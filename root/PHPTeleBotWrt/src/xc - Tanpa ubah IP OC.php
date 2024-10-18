<?php
error_reporting(E_ALL); ini_set('display_errors', 1);
date_default_timezone_set('Asia/Bangkok');

$oc_ip = trim(shell_exec('uci get network.lan.ipaddr'),"\n"); // '192.168.1.1';
$oc_port = trim(shell_exec('uci get openclash.config.cn_port'),"\n"); // '9090';
$oc_secret = trim(shell_exec('uci get openclash.config.dashboard_password'),"\n"); // 'viserion';

function akunOC(){
    $file_path = '/www/tinyfm/openclash/proxy_provider/mix-SG-ID.yaml';
    $pattern = '/[a-z0-9]{16}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/i';
    
    if (file_exists($file_path)) {
        $lines = file($file_path);
        $first_6_lines = array_slice($lines, 0, 6);
        $text = implode('', $first_6_lines);
        
        $result = preg_replace_callback($pattern, function($matches) {
            return '<code>' . $matches[0] . '</code>';
        }, $text);
        
        return $result;  // Output or return the modified text as needed
    } else {
        return "File not found\n";
    }
}

function cekString($text){
    $jumlahChar = 16;
    // Check the length of the original string
    $originalLength = strlen($text);
    
    // If the original string is longer than 20 characters, truncate it
    if ($originalLength > $jumlahChar) {
        // Calculate the number of characters to extract from the left and right of the original string
        $leftLength = floor(($jumlahChar - 3) / 2); // 3 is the length of "..."
        $rightLength = ceil(($jumlahChar - 3) / 2);
        
        // Get the left and right parts of the string and add three dots in the middle
        $limitedString = substr($text, 0, $leftLength) . '...' . substr($text, -$rightLength);
    } else {
        // If the original string is shorter than 20 characters, calculate padding
        $paddingLength = max(0, $jumlahChar - $originalLength);
        $leftPadding = floor($paddingLength / 2);
        $rightPadding = ceil($paddingLength / 2);
        
        // Create the padded string with original string centered
        $limitedString = str_repeat(' ', $leftPadding) . $text . str_repeat(' ', $rightPadding);
    }
    
    // Output the limited/padded string
    return $limitedString."";
}

// echo cekString("adalah anak \n");

function seeURL($url){
    $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        $output = curl_exec($ch);
        curl_close($ch);
        return $output;
}

function delayColor($input){
    if ($input == 0) {
        return "⬛️";
    }elseif ($input >= 1 && $input <= 150) {
        return "🟩";
    }elseif ($input >= 151 && $input <= 300) {
        return "🟨";
    }elseif ($input >= 300 && $input <= 350) {
        return "🟧";
    }elseif ($input > 350) {
        return "🟥";
    }
}

function readXL(){
        $rawConfig = file_get_contents("./xl");
        $raw = explode("\n",$rawConfig);
        $number = $raw[0];
        return $number;
    
}

// function ADB(){

//         // Execute the ADB command for battery status and store the output in a variable
// $battery_status = shell_exec('adb shell dumpsys battery');

// // Execute the ADB command for signal strength and store the output in a variable
// $signal_status = shell_exec('adb shell dumpsys telephony.registry');

// // Execute the ADB command for device model and store the output in a variable
// $device_model = shell_exec('adb shell getprop ro.product.model');

// // android ver
// $android_ver = shell_exec('adb shell getprop ro.build.version.release');

// // Use regular expressions to extract the battery level
// preg_match('/level: (\d+)/', $battery_status, $matches);
// $battery_level = $matches[1];

// // Use regular expressions to extract the battery status numeric value
// preg_match('/status: (\d+)/', $battery_status, $matches);
// $battery_status_numeric = $matches[1];

// // Use regular expressions to extract the signal level
// preg_match('/mSignalStrength=(\d+)/', $signal_status, $matches);
// $signal_level = $matches[1];

// // Trim the device model string to remove whitespaces
// $device_model = trim($device_model);

// // Check the numeric value of the battery status
// if($battery_status_numeric == 2){
//     $battery_status = "Charging";
// }elseif($battery_status_numeric == 3){
//     $battery_status = "Discharging";
// }elseif($battery_status_numeric == 5){
//     $battery_status = "Full";
// }else{
//     $battery_status = "Unknown";
// }

// // Print the battery level, status, signal level and device model
// $result = "ADB Information
// Battery Level   : $battery_level %
// Battery Status  : $battery_status
// Signal Level    : $signal_level
// Device Model    : $device_model
// Android Version : $android_ver";

// return $result;

// }

function MyXL($number){
    if ($number == "") {
        if (readXL() == null) {
            return "Nomor kosong, Setting nomor dengan /setxl 087x";
        }else{
            $data = seeURL("https://sidompul.cloudaccess.host/cek.php?nomor=".readXL());
            return $data;
        } 
    }else{
        $data = seeURL("https://sidompul.cloudaccess.host/cek.php?nomor=$number");
        return $data;
    }
}

// Clash API https://dreamacro.github.io/clash/runtime/external-controller.html
function OCHealtCheck($text = null){
$ch = curl_init();
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
curl_setopt($ch, CURLOPT_ENCODING, 'gzip, deflate');
$headers = array();
$headers[] = 'Authorization: Bearer '. $GLOBALS["oc_secret"] .'';
    if ($text === null) {
        curl_setopt($ch, CURLOPT_URL, 'http://'. $GLOBALS["oc_ip"] .':'. $GLOBALS["oc_port"] . '/providers/proxies/');
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
        $result = curl_exec($ch);
        if (curl_errno($ch)) {
            echo 'Error:' . curl_error($ch);
        }
        curl_close($ch);
        $data = json_decode($result, true);
        $providers = $data['providers'];
        $providersToProcess = array_slice($providers, 0, -1);
        $iterationCount = 0;
        $final = '';
            foreach ($providersToProcess as $provider => $providerData) {
                $groupName = $providerData['name'];
                $channel = array();
                $channel[$iterationCount] = curl_init();
                curl_setopt($channel[$iterationCount], CURLOPT_URL, 'http://'. $GLOBALS["oc_ip"] .':'. $GLOBALS["oc_port"] . '/providers/proxies/' . $groupName . '/healthcheck');
                curl_setopt($channel[$iterationCount], CURLOPT_HTTPHEADER, $headers);
                $result = curl_exec($channel[$iterationCount]);
                if (curl_errno($channel[$iterationCount])) {
                    echo 'Error:' . curl_error($channel[$iterationCount]);
                }
                $httpCode = curl_getinfo($channel[$iterationCount], CURLINFO_HTTP_CODE); // Get HTTP response code
                curl_close($ch);
                $iterationCount++;
                if ($httpCode == 204) {
                    $hasil = "$groupName Success";
                } else {
                    $hasil = "$groupName Failure";
                }
                $final .= "$hasil\n";
            }
        return $final."";
    }
    else{
        curl_setopt($ch, CURLOPT_URL, 'http://'. $GLOBALS["oc_ip"] .':'. $GLOBALS["oc_port"] . '/providers/proxies/' . $text . '/healthcheck');
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
        $result = curl_exec($ch);
        if (curl_errno($ch)) {
            echo 'Error:' . curl_error($ch);
        }
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE); // Get HTTP response code
        curl_close($ch);
        if ($httpCode == 204) {
            return "$text Success\n";
        } else {
            return "$text Failure\n";
        }
    }
}
// echo OCHealtCheck();

// Clash API https://dreamacro.github.io/clash/runtime/external-controller.html
function OpenClashProxies($cekAtauTidak = null){
// Generated by curl-to-PHP: http://incarnate.github.io/curl-to-php/
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'http://'. $GLOBALS["oc_ip"] .':'. $GLOBALS["oc_port"] . '/providers/proxies/');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
curl_setopt($ch, CURLOPT_ENCODING, 'gzip, deflate');

$headers = array();
$headers[] = 'Accept: */*';
$headers[] = 'Accept-Language: en-US,en;q=0.9';
$headers[] = 'Authorization: Bearer '. $GLOBALS["oc_secret"] .'';
$headers[] = 'Connection: keep-alive';
$headers[] = 'Content-Type: application/json';
$headers[] = 'Cookie: filemanager=ee057d392316be9bec05f297f2037536';
$headers[] = 'Referer: http://'. $GLOBALS["oc_ip"] .':'. $GLOBALS["oc_port"] .'/ui/yacd/?hostname='. $GLOBALS["oc_ip"] .'&port='. $GLOBALS["oc_port"] .'&secret='. $GLOBALS["oc_secret"] .'';
$headers[] = 'Sec-Gpc: 1';
$headers[] = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36';
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
$result = curl_exec($ch);
if (curl_errno($ch)) {
    echo 'Error:' . curl_error($ch);
}
curl_close($ch);
$data = json_decode($result,true);
// $data = $data['providers']['default']['proxies']; // ASLI
// $data = $data['providers']['TJ']['proxies']; //Coba select 1 Proxy saja
$providers = $data['providers']; // bagian exclude DIRECT & REJECT
$providersToProcess = array_slice($providers, -1); // bagian exclude DIRECT & REJECT | Kembalikan ke AWAL (SEMUA TAMPIL) ganti ke "array_slice($providers, 0);"
$iterationCount = 0;
$cekHealth = '';
$final = "⏱ Type | Name | Delay | @\n\n";
    foreach ($providersToProcess as $provider => $providerData) { // bagian exclude DIRECT & REJECT
        $groupName = $providerData['name'];
        if ($cekAtauTidak == null){
            $cekHealth .= OCHealtCheck($groupName);
        }
        $proxies = $providerData['proxies']; // bagian exclude DIRECT & REJECT
        foreach ($proxies as $key => $value){
            $name = cekString($value['name']);
            $delay = end($value['history'])['delay'];
            $time = date('H:i', strtotime(end($value['history'])['time'])); //jika menampilkan semua Proxy Group termasuk Direct & Reject akan error karena data 'time' tidak ada
            // $type = $value['type'];
            $color = delayColor($delay);
            $final .= "$color $groupName | $name | $delay ms | $time\n";
        }
    }
return $cekHealth."\n".$final."";
}

function OpenClashRules(){
// Generated by curl-to-PHP: http://incarnate.github.io/curl-to-php/
$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, 'http://'. $GLOBALS["oc_ip"] .':'. $GLOBALS["oc_port"] .'/rules');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');

curl_setopt($ch, CURLOPT_ENCODING, 'gzip, deflate');

$headers = array();
$headers[] = 'Accept: */*';
$headers[] = 'Accept-Language: en-US,en;q=0.9';
$headers[] = 'Authorization: Bearer '. $GLOBALS["oc_secret"] .'';
$headers[] = 'Connection: keep-alive';
$headers[] = 'Content-Type: application/json';
$headers[] = 'Cookie: filemanager=ee057d392316be9bec05f297f2037536';
$headers[] = 'Referer: http://'. $GLOBALS["oc_ip"] .':'. $GLOBALS["oc_port"] .'/ui/yacd/?hostname='. $GLOBALS["oc_ip"] .'&port='. $GLOBALS["oc_port"] .'&secret='. $GLOBALS["oc_secret"] .'';
$headers[] = 'Sec-Gpc: 1';
$headers[] = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36';
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
$result = curl_exec($ch);
if (curl_errno($ch)) {
    echo 'Error:' . curl_error($ch);
}
curl_close($ch);
$data = json_decode($result,true);
$data = $data['rules'];
$final = "Type | Payload | Proxy\n";

    foreach ($data as $key => $value) {
        $proxy = $value['proxy'];
        $payload = $value['payload'];
        $type = $value['type'];
        $final .= "$type | $payload | $proxy \n";
    }
return $final;
}

function myip(){
    $data = json_decode(seeURL("http://ip-api.com/json/"),true);
    $country = $data['country'];
    $countryCode = $data['countryCode'];
    $region = $data['regionName'];
    $city = $data['city'];
    $isp = $data['isp'];
    $timezone = $data['timezone'];
    $as = $data['as'];
    $ip = $data['query'];
    $result = "ISP : $isp\n↳ Address : $as \n↳ IP : <code>$ip</code> \n↳ Region | City : $region | $city \n↳ Timezone : $timezone \n↳ Country : $country | $countryCode";
    return $result;
}

function Speedtest(){

$result = shell_exec('speedtest > result_SpeedTST && cat result_SpeedTST');
return $result;

}
<?php
/**
 * Created by PhpStorm.
 * User: sunmoon
 * Date: 2018/11/21
 * Time: 上午11:33
 */
define('__ICONFONT__', 'iconfont');
define('__CLASS_NAME__', 'AppIcon');
define('__CSS_FILE_NAME__', 'iconfont');

$option = getopt('c:d:f:', ['help']);

$className = $distName = $fontName = '';

function helper_info(){
    echo basename(__FILE__) . ' -c <class_name> -d <dist_name> -f <font_name> --help' . PHP_EOL;
    exit;
}
foreach($option as $key=>$value){
    if('c' == $key){
        $className = trim($value);
    }else if('d' == $key){
        $distName = trim($value);
    }else if('f' == $key){
        $fontName = trim($value);
    }else if('help' == $key){
        helper_info();
    }
}
if('' == $className){
    $className = __CLASS_NAME__;
}
if('' == $distName){
    $distName = __ICONFONT__;
}
if('' == $fontName){
    $fontName = __ICONFONT__;
}


function convert($className, $distName, $fontName){
    echo '开始转换......' . PHP_EOL;
    $date = date('Y-m-d');
    $iconfontCode = <<<eot
/**
 * @Author: sunmoon
 * @Url: http://blog.iw3c.com
 * @Description: Flutter项目自定义字体图标.
 * @Date: {$date}
 */

import 'package:flutter/widgets.dart';
class {$className}{
    static const __FONT_NAME__ = '{$fontName}';
{FLUTTER_CODE}
}
eot;

    $content = file_get_contents(__DIR__ . DIRECTORY_SEPARATOR . 'iconfont' . DIRECTORY_SEPARATOR . __CSS_FILE_NAME__ . '.css');
    //  .icon-delete:before { content: "\e69d"; }
    preg_match_all('/\.icon-(.*?)\:.*?\"(.*?)\";/', $content, $match);
    if(!$match || !isset($match[1]) || empty($match[1])){
        echo '未找到需要转换的字体';
        exit;
    }
    $string = '';
    foreach($match[1] as $key=>$value){
        $name = str_replace('-', '_', trim($value));
        $iconName = strtolower($name);
        $findString = 'static const IconData '.$iconName.' =';
        if(strpos($string, $findString) === false){
            $string .= '    static const IconData '.$iconName.' = const IconData(0x'.trim($match[2][$key]).', fontFamily: __FONT_NAME__);'.PHP_EOL;
        }
    }
    $iconfontCode = str_replace('{FLUTTER_CODE}', $string, $iconfontCode);
    file_put_contents(__DIR__ . DIRECTORY_SEPARATOR . 'dist' . DIRECTORY_SEPARATOR . $distName . '.dart', $iconfontCode);
    echo '转换结束......'.PHP_EOL;
}

convert($className, $distName, $fontName);

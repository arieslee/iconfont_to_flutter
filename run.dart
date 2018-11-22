import 'dart:io';

void main() {
  new Convert();
}

class Convert {
  static const String _const_iconfont = 'iconfont';
  static const String _const_css_file_name = 'iconfont';
  final String class_name = 'AppIcon';
  final String dist_name = 'iconfont';
  final String font_name = 'iconfont';
  Convert() {
    String flutter_code = '''
    /**
 * @Author: sunmoon
 * @Url: http://blog.iw3c.com
 * @Description: Flutter项目自定义字体图标.
 * @Date: {date}
 */

import 'package:flutter/widgets.dart';
class {class_name}{
    static const __FONT_NAME__ = '{font_name}';
{FLUTTER_CODE}
}''';
    // 目录分割符
    String path_separator = Platform.pathSeparator.toString();
    print('开始转换...');
    new File('iconfont${path_separator}${_const_css_file_name}.css')
        .readAsString()
        .then((String content) {
      RegExp exp = new RegExp(r'.icon-(.*?):.*?"\\(.*?)";');
      Iterable<Match> matches = exp.allMatches(content);
      String string = '';
      for (Match m in matches) {
        String icon_name = m.group(1);
        String value = m.group(2);
        int idx = string.indexOf('static const IconData ${icon_name} =');
        if (icon_name != null && value != null && idx < 0) {
          icon_name = icon_name.toLowerCase().replaceAll('-', '_');
          string +=
              '    static const IconData ${icon_name} = const IconData(0x${value}, fontFamily: ${_const_iconfont});\n';
        }
        //print(match);
      }
      List now = new DateTime.now().toString().split(' ');
      flutter_code = flutter_code.replaceFirst('{FLUTTER_CODE}', string);
      flutter_code = flutter_code.replaceFirst('{class_name}', class_name);
      flutter_code = flutter_code.replaceFirst('{font_name}', font_name);
      flutter_code = flutter_code.replaceFirst('{date}', now[0]);
      new File('dist${path_separator}${dist_name}.dart')
          .writeAsString(flutter_code)
          .then((File file) {
        print('转换完成');
      });
    });
  }
}

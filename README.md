# iconfont_to_flutter
Flutter项目中自带有图标 https://docs.flutter.io/flutter/material/Icons-class.html 或者 https://material.io/tools/icons/?style=twotone

但是有些图标难看或者说和我们App的设计风格不太一致，这时候，我们就需要自己找一些图标，导入到Flutter项目中

我们可以在Icon font或者Ico moon上找一些想用的图标下载后，使用此工具，生成Dart类，方便在Flutter项目中使用。


## 使用方法

把下载的字体文件和css文件放到目录iconfont中，dist给可写的权限

#### python版

在命令行中运行

```python
python3 ./run.py
```

####  php版

在命令行中运行

```php
php ./run.php
```

#### 参数说明

|参数|类型|是否必填|描述|默认值|示例|
|:---:|:---:|:---:|:---:|:---:|:---:|
|-c|string|false|生成的dart类的类名|AppIcon|./run.py -cAppIcon|
|-d|string|false|生成的dart类的文件名，不要带.dart后缀|confont|./run.py -diconfont|
|-f|string|false|字体的名称|iconfont|./run.py -ficonfont|
|--help|string|false|帮助| |./run.py --help|

#### 转换完成后如何在Fluter项目中使用

把iconfont目录中的iconfont.ttf复制到flutter项目根目录的一个文件夹中,

如 assets （这个目录和flutter项目中的lib目录同级）

然后打开flutter项目的pubspec.yaml文件，在flutter下面添加

```yaml
  fonts:
    - family: iconfont
      fonts:
        - asset: assets/fonts/iconfont.ttf
```

**_上面参数中的-f，对应family:后面的字体图标名称_**

示例：

```yaml
name: flutter_project
description: A new Flutter project.
version: 1.0.0+1

environment:
  sdk: ">=2.0.0-dev.68.0 <3.0.0"

dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^0.1.2

dev_dependencies:
  flutter_test:
    sdk: flutter

flutter:
  uses-material-design: true
  fonts:
    - family: iconfont
      fonts:
        - asset: assets/fonts/iconfont.ttf
```

#### Flutter代码

```dart
import 'package:flutter/material.dart';
import 'package:demo_project/iconfont.dart';
......
new Icon(AppIcon.home);
or 
new Icon(IconData(0xe6d7, fontFamily: "iconfont")
......
```

# 第５章　ナビゲーション
## 概要
作成中

## ディレクトリ構成
- **[amcl_subscriber](amcl_subscriber)**: /amclと/odomをサブスクライブするパッケージ
- **[kachaka_lidar](kachaka_lidar)**: シンプルなLidarパッケージとドアオープンのサンプル
- **[kachaka_move](kachaka_move)**: シンプルな移動パッケージ
- **[kachaka_teleop](kachaka_teleop)**: 自作遠隔操作パッケージ
- **[map](map)**: 地図ファイルを格納するディレクトリ
- **[path_planning](path_planning)**: 経路計画のサンプルプログラム
- **[waypoint_navi](waypoint_navi)**: ウェイポイントナビゲーションのサンプルパッケージ

## インストール(作成中)
Chapter5の全パッケージを以下のコマンドでインストールします．
- ROSのワークスペースを`~/athome_ws`とする．
  ```
  cd ~/athome_ws/src
  ```

- Chapter5のリポジトリを入手
  ```
  git clone https://github.com/At-Home-Book/chapter5.git
  ```

## 補足情報
- ナビゲーション関連のサンプルプログラムを実行するときは，以下の説明に従って事前に地図ファイルをインストールしてください．  
  - [https://github.com/○○/chapter5/tree/main/map](https://github.com/○○/chapter5/tree/main/map) 

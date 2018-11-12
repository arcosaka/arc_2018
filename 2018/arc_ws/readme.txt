#まず、このパスで以下のコマンドを実行
cd （ここのパス）
catkin_make
source devel/setup.bash

#それぞれのファイルの簡単な説明
src/tama/scripts/brain.py : コントローラーに該当。
　　　　　　　　　　　　　　 このファイルを編集することで送られてくるメッセージを意図的に変更可能

src/tama/scripts/arm.py : アームに該当。
src/tama/scripts/foot.py : モーターに該当。
　　　　　　　　　　　　　
#実行確認は下記それぞれのコマンドで可能
##それぞれ確認前にpigpio deamonを起動しておくこと
sudo pigpiod
##roscoreを起動。別Terminalで実行するか、最後に&をつける
roscore &
##arm用
roslaunch tama arm.launch
##foot用
roslaunch tama foot.launch

#命名規則
変数:小文字始まり、区切りは_
定数:すべて大文字、区切りは_
関数:小文字始まり、区切りは大文字

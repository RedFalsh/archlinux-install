qt安装过程：
1、下载linux版本qt-opensource：
下载地址：
	1. 所有Qt版本下载地址：

	http://download.qt.io/archive/qt/

	2. 所有Qt Creator下载地址：

	http://download.qt.io/archive/qtcreator/

	3. 所有Qt VS开发插件下载地址:

	http://download.qt.io/archive/vsaddin/

	4. Qt相关下载大全

	http://download.qt.io/

2、cd到你下载的目录下：
	sudo chmod a+x qt-opensource-linux-x86-5.5.0.run
	sudo ./qt-opensource-linux-x86-5.5.0.run
这里会弹出框qt安装对话框，按照对话框提示安装就可以了，默认会安装在/opt/目录下，如：/opt/Qt5.5.0/5.5/gcc.....
3、修改.bashrc文件
	sudo vi ~/.bashrc
	在文件末尾添加：
	#QT
	export QTDIR=/opt/Qt5.5.0/5.5/gcc/      #这里是你安装的qt文件gcc目录
	export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${QTDIR}/lib
	export PATH=${QTDIR}/bin:${PATH}

4、将你安装的qt的qmake替换默认的qmake
	sudo ln -s /opt/Qt5.5.0/5.5/gcc/bin/qmake /usr/bin/qmake


sip安装命令：sudo apt-get install sip-dev

pycharm安装过程：
1. 下载
	http://www.jetbrains.com/pycharm/download/

	选择Linux Tab，选择下载免费的Community Edition【1】。当前版本是3.4

 
2. 安装PyCharm

	按照官网给出的安装指导【2】进行安装。

	（1） Copy the pycharm-*.tar.gz to the desired installation location (make sure you have rw permissions for that directory)

	$ cd Downloads/

	（2）Unpack the pycharm-*.tar.gz using the following command: tar xfz pycharm-*.tar.gz

	$ tar xfz pycharm-*.tar.gz

	（3）Remove the pycharm-*.tar.gz to save disk space (optional)

	$ rm  pycharm-*.tar.gz

	（4）Run pycharm.sh from the bin subdirectory

	$ cd pycharm-community-3.4.1/bin/

	$ ./pycharm.sh

	但是安装开始，出现如下错误（弹出的错误对话框）：

	ERROR: Cannot start PyCharm

	No JDK found. Please validate either PYCHARM_JDK, JDK_HOME or JAVA_HOME environment variable points to valid JDK installation.
	
	这里说明要安装JAVA的jdk才行，jdk安装步骤参见ubuntu java jdk安装过程
3. 安装完成后即可应用
4. 附录：
	ui设计文件转换py文件：
		pyuic5安装命令：sudo apt-get install pyqt5-dev-tools
		自己建个py文件，放在你的工程目录下，运行即可：
		import os
		#ui文件转py文件，这里要安装pyuic5
		path_ui = '/home/xiong/PycharmProjects/nt2000_test/ui.ui'#ui文件绝对目录
		paty_py = '/home/xiong/PycharmProjects/nt2000_test/ui.py'#要转换成的py文件绝对目录，原先没有会自己生成
		os.system('pyuic5 -o %s %s'%(paty_py,path_ui))#执行命令

ubuntu java jdk安装过程：
1.官网下载JDK　　　
    地址: http://www.oracle.com/technetwork/articles/javase/index-jsp-138363.html
　　选择相应的 .gz包下载 

2. 解压缩,放到指定目录(以jdk-8u112-linux-i586.tar.gz为例)
	创建目录:
	sudo mkdir /usr/lib/jvm
	解压缩到该目录（cd到jdk-8u112-linux-i586.tar.gz文件目录解压）:
	sudo tar -zxvf jdk-8u112-linux-i586.tar.gz -C /usr/lib/jvm

3.修改环境变量:　　
	sudo vim ~/.bashrc
　	文件的末尾追加下面内容:
	#set oracle jdk environment
	export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_112  ## 这里要注意目录要换成自己解压的jdk 目录
	export JRE_HOME=${JAVA_HOME}/jre  
	export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib  
	export PATH=${JAVA_HOME}/bin:$PATH  
	使环境变量马上生效：
	source ~/.bashrc
4.设置系统默认jdk 版本
	sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk1.8.0_112/bin/java 300  
	sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk1.8.0_112/bin/javac 300  
	sudo update-alternatives --install /usr/bin/jar jar /usr/lib/jvm/jdk1.8.0_112/bin/jar 300   
	sudo update-alternatives --install /usr/bin/javah javah /usr/lib/jvm/jdk1.8.0_112/bin/javah 300   
	sudo update-alternatives --install /usr/bin/javap javap /usr/lib/jvm/jdk1.8.0_112/bin/javap 300   
	然后执行:
	sudo update-alternatives --config java
    	若是初次安装jdk,会有下面的提示：     

   	There is only one alternative in link group java (providing /usr/bin/java): 
    	/usr/lib/jvm/jdk1.8.0_112/bin/java

　	否者,选择合适的jdk

5.测试jdk
	java -version
		java version "1.8.0_112"
		Java(TM) SE Runtime Environment (build 1.8.0_112-b15)
		Java HotSpot(TM) Server VM (build 25.112-b15, mixed mode)
6.jdk 安装成功

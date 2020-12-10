Inspired by [this funny video](https://www.instagram.com/p/CHwWTzshr28/) (Source: unknown). <br/>
Just a practice to implement it by QtPy5. <br/>

![](https://i.imgur.com/oKN9Dbp.gif)

## How to run it
Install the required shared libraries for PyQt5.
```
# apt-get install libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-xfixes0 libxcb-xinerama0 libxcb-xkb1 libxkbcommon-x11-0 libxkbcommon0
```

Clone this project and run it in virtual environment.
```
# git clone https://github.com/KennyTzeng/Resignation-Letter.git
# cd Resignation-Letter/
# python3 -m venv venv
# source venv/bin/activate
(venv)# pip install --upgrade pip
(venv)# pip install PyQt5
(venv)# python3 main.py
```

## Others
[https://hackmd.io/@KennyTseng/HJqBqHIcP](https://hackmd.io/@KennyTseng/HJqBqHIcP)
Here are some notes I wrote when doing this project, including:
+ Trouble shooting of running PyQt5 in Windows subsystem ubuntu 18.04 (WSL)
+ GUI design - Qt Designer
+ How did I test the sub-component
+ References

## Resources
+ letter icon: made by [DinosoftLabs](https://www.flaticon.com/authors/dinosoftlabs) from [www.flaticon.com](https://www.flaticon.com/)
+ warning icon: made by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](https://www.flaticon.com/)
+ X-mark icon: from [www.iconsdb.com](https://www.iconsdb.com/red-icons/x-mark-3-icon.html)
+ green-ok-mark icon: from [www.iconsdb.com](https://www.iconsdb.com/green-icons/ok-icon.html)

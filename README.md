# JPG_folder_to_animated_gif
Converting JPG files in a folder to an animated GIF file.

## 개발환경
- Windows 10 WSL

## 참고문헌
- [ Python ] jpg, png 를 gif 또는 mp4로 만들기
    - https://data-newbie.tistory.com/413
- 파이썬 GIF 애니메이션 만들기 예제 코드 (Python imageio)
    - https://muzukphysics.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-GIF-%EC%95%A0%EB%8B%88%EB%A9%94%EC%9D%B4%EC%85%98-%EB%A7%8C%EB%93%A4%EA%B8%B0-%EC%98%88%EC%A0%9C-%EC%BD%94%EB%93%9C-Python-imageio

## WSL에서 Python 가상환경 만들기
- https://docs.microsoft.com/ko-kr/windows/python/web-frameworks
- Python3 버전 확인
    ~~~
    $ python3 --version
    ~~~
    ~~~
    apple@KDY-SB2:~/JPG_folder_to_animated_gif$ python3 --version
    Python 3.6.9
    ~~~
- pip 설치
    ~~~
    $ sudo apt update && sudo apt upgrade
    $ sudo apt install python3-pip
    ~~~

## imageio 패키지 설치
- imageio라는 패키지 설치 확인
    ~~~
    (gif) C:\WINDOWS\system32>python
    Python 3.9.12 (main, Apr  4 2022, 05:22:27) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import imageio
    >>> imageio.__version__
    '2.9.0'
    >>>
    ~~~

- imageio 설치
    - https://anaconda.org/conda-forge/imageio
    ~~~
    > conda activate gif
    > conda install -c conda-forge imageio
    ~~~

## GitHub Repository clone 및 Visual Studio Code 실행
- git clone
    ~~~
    $ cd ~
    $ git clone https://github.com/hiddensword/JPG_folder_to_animated_gif.git
    ~~~
- wsl을 위한 git branch 만들기
    ~~~
    $ git branch wsl_18.04
    ~~~
    ~~~
    apple@KDY-SB2:~/JPG_folder_to_animated_gif$ git branch wsl_18.04
    apple@KDY-SB2:~/JPG_folder_to_animated_gif$ git branch
    * main
      wsl_18.04
    ~~~
- git branch 전환하기
    ~~~
    $ git checkout wsl_18.04
    ~~~
- git commit하기
    ~~~
    $ git add README.md
    ~~~
- Visual Studio Code에서 interpreter 선택
    - `Ctrl + Shift + p`(command pallet)를 누른 후, `Python: Select Interpreter`를 선택
    - `+ Enter interpreter path ...` 선택
    - `Find ...` 선택    
    - `C:\ProgramData\Anaconda3\envs\gif` 경로로 입력
    - `python.exe` 선택

## (참고) apt-upgrade중 에러
~~~
Segmentation fault (core dumped)
dpkg: error processing package libc-bin (--configure):
 subprocess installed post-installation script returned error exit status 139
Errors were encountered while processing:
 libc-bin
E: Sub-process /usr/bin/dpkg returned an error code (1)
~~~
- https://blog.miyu.pe.kr/i/entry/953
- dpkg의 관련 정보를 삭제해주고 다시 받으면 된다.
    ~~~
    rm  /var/lib/dpkg/info/libc-bin.*

    apt-get clean
    apt-get update
    apt-get upgrade
    ~~~
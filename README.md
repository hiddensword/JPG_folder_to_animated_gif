# JPG_folder_to_animated_gif
Converting JPG files in a folder to an animated GIF file.

## 개발환경
- Windows 10

## 참고문헌
- [ Python ] jpg, png 를 gif 또는 mp4로 만들기
    - https://data-newbie.tistory.com/413
- 파이썬 GIF 애니메이션 만들기 예제 코드 (Python imageio)
    - https://muzukphysics.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-GIF-%EC%95%A0%EB%8B%88%EB%A9%94%EC%9D%B4%EC%85%98-%EB%A7%8C%EB%93%A4%EA%B8%B0-%EC%98%88%EC%A0%9C-%EC%BD%94%EB%93%9C-Python-imageio

## Anaconda 가상환경 설정
- Anaconda Prompt를 관리자 권한으로 실행
- 가상환경 목록 확인
    ~~~
    > conda env list
    ~~~
    ~~~
    (base) C:\WINDOWS\system32>conda env list
    # conda environments:
    #
    base                  *  C:\ProgramData\Anaconda3
    ~~~
- 새 가상환경 `gif`를 생성
    ~~~
    > conda create -n gif python anaconda
    ~~~
- 가상환경 활성화
    ~~~
    > conda activate gif
    ~~~
    ~~~
    (base) C:\WINDOWS\system32>conda activate gif

    (gif) C:\WINDOWS\system32>python
    Python 3.9.12 (main, Apr  4 2022, 05:22:27) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ~~~
- 가상환경 비활성화
    ~~~
    > conda deactivate
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
- GitHub Desktop 활용
- Visual Studio Code에서 interpreter 선택
    - `Ctrl + Shift + p`(command pallet)를 누른 후, `Python: Select Interpreter`를 선택
    - `+ Enter interpreter path ...` 선택
    - `Find ...` 선택    
    - `C:\ProgramData\Anaconda3\envs\gif` 경로로 입력
    - `python.exe` 선택
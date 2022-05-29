#-*- coding: utf-8 -*-

import os
import imageio

def convert(path_input, path_output, file_type, fps, save_gif_name) :

    images = []

    for file_name in os.listdir(path_input) :
        if file_name.endswith('.{}'.format(file_type)):

            # 확인을 위한 사진 파일명 출력
            print(file_name)

            file_path = os.path.join(path_input, file_name)
            images.append(imageio.imread(file_path))

    # gif로 출력
    imageio.mimsave('{}/{}.gif'.format(path_output, save_gif_name), \
        images, fps)
    print('{}.gif is saved.\n'.format(save_gif_name))


if __name__ == "__main__" :
    print("")
    print("=========================")
    print(" Converting JPG files in a folder")
    print(" to an animated GIF file.")
    print("=========================")
    print("")

    path_input = r'C:/DeepExpress_traversability/220529_kdy_gif/output_2022-05-10-17-06-56/frame0168' # 사진 디렉토리
    path_output = r'C:/DeepExpress_traversability/220529_kdy_gif/output_2022-05-10-17-06-56' # 사진 디렉토리
    file_type = r'jpg'  # 사진 확장자
    fps = 10 # 사진 넘기는 framerate
    save_gif_name = r'frame0168' # 완성 gif 이름
    
    convert(path_input, path_output, file_type, fps, save_gif_name)
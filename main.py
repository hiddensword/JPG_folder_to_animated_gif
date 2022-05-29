#-*- coding: utf-8 -*-

import os
import imageio

def convert(path_input, path_output, file_type, save_gif_name) :

    images = []
    count = 0

    for file_name in os.listdir(path_input) :
        if file_name.endswith('.{}'.format(file_type)):

            # 확인을 위한 사진 파일명 출력
            #print(file_name)

            file_path = os.path.join(path_input, file_name)
            images.append(imageio.imread(file_path))
            count = count + 1   # 불러드린 사진 파일 갯수 누적

    print('{} images were loaded.'.format(count))
    print('\nPlease wait for saving your large animated GIF file.')

    # gif로 출력
    imageio.mimsave('{}/{}.gif'.format(path_output, save_gif_name), \
        images, fps=10)
    print('{}.gif is saved.\n'.format(save_gif_name))


if __name__ == "__main__" :
    print("")
    print("=========================")
    print(" Converting JPG files in a folder")
    print(" to an animated GIF file.")
    print("=========================")
    print("")

    #path_input = r'C:/DeepExpress_traversability/220529_kdy_gif/output_2022-05-10-17-06-56/frame0168' # 사진 디렉토리
    path_input = r'/mnt/c/DeepExpress_traversability/gif/output_2022-05-10-17-44-45/frame0579'
    #path_output = r'C:/DeepExpress_traversability/220529_kdy_gif/output_2022-05-10-17-06-56' # 사진 디렉토리
    path_output = r'/mnt/c/DeepExpress_traversability/gif/output_2022-05-10-17-44-45'
    file_type = r'jpg'  # 사진 확장자
    save_gif_name = r'frame0579' # 완성 gif 이름
    
    convert(path_input, path_output, file_type, save_gif_name)
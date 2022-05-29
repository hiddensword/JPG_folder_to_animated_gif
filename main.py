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

    file_type = r'jpg'  # 사진 확장자

    #========================
    # output_2022-05-10-17-06-56'

    path_output = r'/mnt/c/DeepExpress_traversability/gif/output_2022-05-10-17-06-56'
    path_input = path_output + '/'

    save_gif_name = r'frame0168' # 완성 gif 이름
    path = path_input + save_gif_name
    convert(path, path_output, file_type, save_gif_name)
    print(path)
    
    #convert(path_input, path_output, file_type, save_gif_name)
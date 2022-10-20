from __future__ import print_function

import logging
import os

import gphoto2 as gp

class Camera:

    def capturar_imagem(self):
        try:
            logging.basicConfig(
                format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
            callback_obj = gp.check_result(gp.use_python_logging())
            camera = gp.Camera()
            camera.init()
            print('Capturing image')
            file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
            print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
            target = os.path.join('temp/img', file_path.name)
            print('Copying image to', target)
            camera_file = camera.file_get(
                file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
            camera_file.save(target)
            camera.exit()
            return 0
        except gp.GPhoto2Error as e:
            print('Erro ao carregar uma biblioteca: ', e)
            print('Certifique-se que a variável iolibs foi especificada.')
        except Exception as e:
            print('Erro desconhecido:', e)

    def detectar_camera(self):
        try:
            logging.basicConfig(
                format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
            callback_obj = gp.check_result(gp.use_python_logging())
            detectar = gp.gp_camera_autodetect()[0]
            # Testa câmera
            if detectar == 1:
                resultado = 'Conectada'
                return resultado
            elif detectar == 0:
                resultado = 0
                return resultado
            elif detectar == -4:
                resultado = 'Erro -4: Não foi possível carregar biblioteca.'
                print('Erro ao carregar uma biblioteca.')
                print('Certifique-se que a variável iolibs foi especificada.')
                return resultado
            else:
                print('Erro inesperado. Contacte o suporte.', detectar)


        except gp.GPhoto2Error as e:
            print('Erro ao carregar uma biblioteca: ', e)
            print('Certifique-se de que a variável iolibs foi especificada.')

        except IndexError as e:
            print('Erro de Index:', e)
            print('A câmera não foi identificada.')
            print('Certifique-se de que a câmera está conectada e a variável "camlibs" especificada.')

        except Exception as e:
            print('Erro desconhecido:', e)

    def nome_camera(self):
        try:
            logging.basicConfig(
                format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
            callback_obj = gp.check_result(gp.use_python_logging())
            cameras = gp.Camera.autodetect()
            for n, (name, value) in enumerate(cameras):
                print(name)
                return name

        except gp.GPhoto2Error as e:
            print('Erro ao carregar uma biblioteca: ', e)
            print('Certifique-se de que a variável iolibs foi especificada.')

        except IndexError as e:
            print('Erro de Index:', e)
            print('A câmera não foi identificada.')
            print('Certifique-se de que a câmera está conectada e a variável "camlibs" especificada.')

        except Exception as e:
            print('Erro desconhecido:', e)

    def configurar_camera(self, tipo_config, valor):
        """

        :param tipo_config: STRING
        :param valor: STRING
        :return:

        Abertura = aperture
        ISO = iso
        Vel. disparo = shutterspeed
        WB ajuste A = whitebalanceadjusta
        WB ajuste B = whitebalanceadjustb
        Pict Style = picturestyle
        Compensação exp. = aeb

        """
        # use Python logging
        logging.basicConfig(
            format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
        callback_obj = gp.check_result(gp.use_python_logging())
        # open camera connection
        camera = gp.check_result(gp.gp_camera_new())
        gp.check_result(gp.gp_camera_init(camera))
        # get configuration tree
        config = gp.check_result(gp.gp_camera_get_config(camera))
        # find the capture target config item
        capture_target = gp.check_result(
            gp.gp_widget_get_child_by_name(config, tipo_config))
        # print possible settings
        for n in range(gp.check_result(gp.gp_widget_count_choices(capture_target))):
            choice = gp.check_result(gp.gp_widget_get_choice(capture_target, n))
            if valor == choice:
                print('Choice:', n, choice)
                # set value
                value = gp.check_result(gp.gp_widget_get_choice(capture_target, n))
                gp.check_result(gp.gp_widget_set_value(capture_target, value))
                # set config
                gp.check_result(gp.gp_camera_set_config(camera, config))
        # clean up
        gp.check_result(gp.gp_camera_exit(camera))
        return 0
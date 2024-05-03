import pygame
import os

# Inicialização do Pygame
pygame.init()

# Configuração da janela
largura = 240
altura = 250
janela = pygame.display.set_mode((largura, altura))

# Diretório atual do script
diretorio_atual = os.path.dirname(__file__)

# Caminho para os arquivos de frames e áudio
caminho_frames = os.path.join(diretorio_atual, "frames")
caminho_audio = os.path.join(diretorio_atual, "audio")

# Carregamento das imagens dos frames
frames = []
for i in range(81):  # Todas as imagens estão numeradas como frame_ 0 a 80
    filename = os.path.join(caminho_frames, "frame_{}.png".format(i))
    frame = pygame.image.load(filename)
    frames.append(frame)

# Carregamento do arquivo de som
pygame.mixer.music.load(os.path.join(caminho_audio, "LuizGonzaga.mp3"))

# Definição de variáveis
frame_atual = 0
clock = pygame.time.Clock()
fps = 10  # Frames por segundo (0,5 segundos entre cada frame)

# Reproduzir o som
pygame.mixer.music.play()

# Loop principal do desenho
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Verificação da mudança de frame
    frame_atual = (frame_atual + 1) % len(frames)  # Loop contínuo dos frames

    # Desenho do frame atual na janela
    janela.blit(frames[frame_atual], (0, 0))

    # Atualização da tela
    pygame.display.flip()

    # Limitação de FPS
    clock.tick(fps)

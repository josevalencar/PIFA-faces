# PIFA-faces: O Detectador de Faces da Bola de Ouro PIFA 2024

![Output com falso positivo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGYydnk3bGZsd2hmMGU2ZnJlMGs2ZXk3YjU0b25xNnM2cHFpbmYzMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/foqA57rGiXHudZPtZm/giphy.gif)

Este repositório detalha um sistema de detecção de faces para a cerimônia da Bola de Ouro da PIFA de 2024

# Perguntas técnicas
## Método de detecção escolhido 
O Haar Cascade foi o método escolhido para esse sistema. O algoritmo Haar Cascade é uma técnica poderosa e eficiente para a detecção de objetos em imagens, como rostos, carros, e outros objetos comuns. Ele utiliza uma série de características simples, chamadas de "Haar-like features", que são calculadas de forma rápida usando uma imagem integral.  são retângulos simples que calculam diferenças de intensidades entre regiões claras e escuras na imagem. No geral, esse algoritmo se baseia em três componentes principais: **Imagem Integral**, uma representação da imagem que permite cálculos rápidos. **Seleção de Características**, usa o algoritmo AdaBoost para selecionar as características mais importantes. **Cascade de Classificadores**, uma série de classificadores que processam a imagem em etapas. Essa estrutura em cascata consiste em vários estágios de classificadores, onde cada estágio rejeita rapidamente regiões da imagem que não são de interesse.

Neste repositório, há um arquivo .xml que justamente define essa estrutura de cascata para detectar as imagens de interesse. Especificamente para este projeto, o arquivo .xml é para detectar faces frontais, que são as mais presentes no arquivo la_cabra.mp4. 

## Classificação 
Classificando em ordem as possibilidades de implementação em termos de viabilidade técnica (se é possível resolver o problema), facilidade de implementação e versatilidade da solução, temos: 

1. HAAR Cascade

É o melhor para esse problema pois pegamos uma ferramenta já treinada em várias (e muitas) imagens e só aplicamos ao nosso vídeo. Além de fácil, é rápido. 

2. CNN

CNN (Convolutional Neural Networks) funcionam aqui mas não se encaixam bem nesse escopo tendo em vista que para reconhecer os rostos, teríamos que treinar a rede neural com um dataset muito grande para reconhecer os rostos. Chato pra achar dataset e demora pra treinar. PORÉM, é muito efetivo. Por isso fica no segundo lugar. 

3. Filtros de correlação cruzada

Este método seria eficaz caso quiséssemos detectar apenas um rosto específico (do Messi, por exemplo). Aí, poderíamos utilizar o rosto dele como um filtro. Porém, como nesse caso são todas faces do vídeo, não se encaixa nesse espoco tão bem. Mas funcionam. 

4. NN Linear

Coloquei em último lugar pelo fato de que as Neural Networks Lineares resolvem problemas... linearmente. Sendo assim, se imaginarmos cada pixel da imagem como um input da rede neural e que estamos trabalhando com vídeos, talvez não teria uma eficácia muito boa. 


## Nova classificação
Agora, classificando a detecção de emoções através da imagem de uma face. 

1. CNN 

Caso queiramos classificar emoções através de uma imagem apenas, as CNNs são uma ótima opção pois podemos pegar um dataset classificado, treinar um modelo com as principais emoções e através de uma imagem de uma face dizer qual é a emoção

2. NN Linear

Tendo em vista que estamos classificando o que está presente em apenas uma image, as NNs Lineares funcionam neste cenário. Apesar de serem mais rápidas, são menos eficazes pois extraem menos features da imagem. 

3. HAAR

Não servem tanto pois apenas classificam um por vez de forma indidivual. Por exemplo, quem está sorrindo na imagem. 

4. Filtros de correlação cruzada

Aqui seria caso quiséssemos uma emoção de alguém em específico em uma imagem, utilizando como filtro. Acaba não sendo muito útil. 


## Variações
Nesta lógica de implementação as soluções apresentadas não possuem a capacidade de considerar variações de um frame pra outro pois atualmente pegamos cada frame e verificamos o rosto, não passando nenhuma informação para o próximo frame. Talvez, uma possível implementação para isso seria uma rede neural que, a cada frame, consiga passar informações como inputs para outra. E com essa informação, teria mais probabilidade e assertividade na detecção. 

## Bônus - Quem Ganha a Bola de Ouro 2024?
Não sei quem ganha, MAS *esse* cara [aqui](https://github.com/rmnicola) merece. 

# Como executar 
Rode os comandos: 

* Ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Rode o arquivo:
```bash
python3 main.py
```
Abra o vídeo com nome "output.mp4" nos arquivos. 

# Outros

Além de detectar faces utilizando o método escolhido, há uma estratégia clara implementada para evitar falsos positivos: 

```python
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(70, 70))
    faces_2 = face_cascade2.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(70, 70))

    for (x, y, w, h) in faces:
        if (x, y, w, h) in faces_2:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
 ```

Aqui inserimos uma segunda cascata e fazemos uma verificação se as faces reconhecidas na primeira cascata também estão na segunda cascata. E este é o resultado final sem falsos positivos: 

![Output definitivo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzNvN2Zjd3E2MGFwNmYwcGF3MTB2YzdhMTR1eDQ5a3JleWY0MGhsYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oFZiPG1M1AD5qEpGVq/giphy.gif)

Pode-se observar os dois resultados nos arquivos output_deinitivo.mp4 e output_falso_positivo.mp4

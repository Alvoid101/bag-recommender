# Sistema recomendador de bolsos para dama basado en el color


<img width="800" height="300" alt="Banner" src="https://github.com/user-attachments/assets/9feac9cb-2b45-4acd-9584-e8ee959369d7" />

Recomendador inteligente de bolsos desarrollado con técnicas de machine learning y visión por computadora. Incluye extracción de características visuales y clasificación mediante SVM, ademas icluye agrupamiento mediante Kmeans.

## Autores

[Helbert Alexeiv Correa Uribe](https://github.com/Alvoid101), [Ivan Ramiro Suarez Diaz](https://github.com/IvanRamiro05), [Alejandro Salazar Rincon](https://github.com/alejosarin1)

## Objetivo

Desarrollar un sistema inteligente capaz de recomendar bolsos similares utilizando análisis de características visuales (principalmente color), mediante el uso de técnicas de aprendizaje no supervisado y modelos de clasificación, con el fin de mejorar la experiencia del usuario al buscar productos relacionados.

## Dataset
### fashion product images small

El dataset mecha2019/fashion-product-images-small es una colección de aproximadamente 42.000 productos de moda, cada uno con una imagen (vía URL) y metadatos estructurados como tipo de prenda, color base, temporada, uso, categoría, género y nombre de producto. Está en formato Parquet, lo que facilita su procesamiento. La licencia es desconocida, por lo que se debe tener precaución en su uso para fines comerciales. Debido a su riqueza visual y semántica, es ideal para tareas de clasificación, análisis de moda y recomendación multimodal.

[Dataset](https://huggingface.co/datasets/mecha2019/fashion-product-images-small)

## Modelos

### Machine Learning - Clasificación

#### Modelos probados

- Gaussian Naive Bayes
- Decision Tree Classifier
- Random Forest Classifier
- Deep Learning
- Support Vector Machine (Mejor modelo supervisado para el proyecto)

### Reducción de Dimensionalidad

- PCA
- t-SNE (Mejor tecnica para el proyecto)

### Clustering

- K-Means (Mejor modelo no supervisado para el proyecto)
- DBSCAN

## Enlaces
- [Codigo principal](https://github.com/Alvoid101/bag-recommender/blob/main/5.Clustering.ipynb).
- [Codigo pagina web](https://github.com/Alvoid101/bag-recommender/tree/main/src/ganchoBGA).
- [Video](https://www.youtube.com/watch?v=kadm-wfqA3Y).
- [Repositorio](https://github.com/Alvoid101/bag-recommender/tree/main).

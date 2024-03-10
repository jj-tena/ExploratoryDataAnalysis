import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

class ExploratoryDataAnalysis:
  """
  Clase para realizar un análisis exploratorio de datos en un DataFrame de pandas.

  Parámetros:
  - dataset (pd.DataFrame): El conjunto de datos a analizar.

  Métodos:
  - setDescription(self, description: str) -> None: Establece la descripción del conjunto de datos.
    - getDescription(self) -> str: Devuelve la descripción del conjunto de datos.
    - getShape(self) -> tuple: Devuelve la forma (número de filas y columnas) del conjunto de datos.
    - getSize(self) -> int: Devuelve el tamaño total del conjunto de datos.
    - getHead(self) -> pd.DataFrame: Devuelve las primeras filas del conjunto de datos.
    - getColumns(self) -> list: Devuelve los nombres de las columnas del conjunto de datos.
    - getTypes(self) -> pd.Series: Devuelve los tipos de datos de cada columna.
    - getStatistics(self) -> pd.DataFrame: Devuelve estadísticas descriptivas del conjunto de datos.
    - getNulls(self) -> pd.Series: Devuelve la cantidad de valores nulos por columna.
    - getBoxplots(self) -> None: Genera boxplots para visualizar la distribución de las variables.
    - getUniques(self) -> pd.Series: Devuelve la cantidad de valores únicos por columna.
    - countUniques(self) -> str: Devuelve la cuenta de valores únicos para cada columna.
    - getHistograms(self, nBins: int) -> None: Genera histogramas para visualizar la distribución de las variables.
    - getCorrelationMatrix(self) -> None: Genera y muestra la matriz de correlación entre variables.
    - getAutomaticStatisticalEDA(self) -> None: Realiza un análisis estadístico automático utilizando la biblioteca Sweetviz.
    - getAutomaticGraphicalEDA(self) -> None: Realiza un análisis gráfico automático utilizando la biblioteca AutoViz.
    - get_numeric_columns(self) -> pd.Index: Devuelve las columnas numéricas del conjunto de datos.
    - get_categorical_columns(self) -> pd.Index: Devuelve las columnas categóricas del conjunto de datos.
    - plot_bar_charts_categorical_columns(self) -> None: Genera gráficos de barras para variables categóricas.
  """

  def __init__(self, dataset: pd.DataFrame) -> None:
    """
    Inicializa la clase con el conjunto de datos.

    Parámetros:
      - dataset (pd.DataFrame): El conjunto de datos a analizar.
    """
    self.dataset = dataset

  def setDescription(self, description: str) -> None:
    """
    Establece la descripción del conjunto de datos.

    Parámetros:
      - description (str): La descripción del conjunto de datos a analizar.
    """
    self.description = description
  
  def getDescription(self) -> str:
    """
    Devuelve la descripción del conjunto de datos.
    """
    return self.description
  
  def getShape(self) -> str:
    """Devuelve la forma (número de filas y columnas) del conjunto de datos."""
    return (self.dataset.shape)

  def getSize(self) -> str:
    """Devuelve el tamaño total del conjunto de datos."""
    return (self.dataset.size)

  def getHead(self) -> pd.DataFrame:
    """Devuelve las primeras filas del conjunto de datos."""
    return (self.dataset.head())

  def getColumns(self) -> list:
    """Devuelve los nombres de las columnas del conjunto de datos."""
    return (self.dataset.columns)

  def getTypes(self) -> str:
    """Devuelve los tipos de datos de cada columna."""
    return (self.dataset.dtypes)

  def getStatistics(self) -> pd.DataFrame:
    """Devuelve estadísticas descriptivas del conjunto de datos."""
    return (self.dataset.describe())
  
  def getNulls(self) -> str:
    """Devuelve la cantidad de valores nulos por columna."""
    return (self.dataset.isnull().sum())

  def get_numeric_columns(self):
    """Devuelve las columnas numéricas del conjunto de datos."""
    numeric_cols = self.dataset.select_dtypes(include=['float64', 'int64']).columns
    return numeric_cols

  def getBoxplots(self) -> None:
    """
    Genera boxplots para visualizar la distribución de las variables.
    """
    num_cols = 3
    num_rows = math.ceil(len(self.get_numeric_columns()) / num_cols)
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(12, 4 * num_rows))
    numeric_variables = self.get_numeric_columns()
    variable_index = 0
    for i in range(num_rows):
      for j in range(num_cols):
        if variable_index < len(numeric_variables):
          variable = numeric_variables[variable_index]
          self.dataset[variable].plot(kind='box', ax=axs[i, j])
          axs[i, j].set_title(variable)
          variable_index += 1
        else:
          axs[i, j].axis('off')
    plt.tight_layout()
    plt.show()

  def getUniques(self) -> str:
    """Devuelve la cantidad de valores únicos por columna."""
    return (self.dataset.nunique())

  def countUniques(self) -> str:
    """
    Devuelve la cuenta para cada valor único en cada columna.
    """
    result = ""
    for col in self.getColumns():
      result += f"\nColumna: {col}\n{self.dataset[col].value_counts()}\n"
    return result

  def getHistograms(self, nBins: int = 10) -> None:
    """
    Genera histogramas para visualizar la distribución de las variables numéricas.
    Parámetros:
    - nBins (int): Número de bins (contenedores) para el histograma. Por defecto, se establece en 10.
    """
    num_cols = 3
    num_rows = math.ceil(len(self.get_numeric_columns()) / num_cols)
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(12, 4 * num_rows))
    numeric_variables = self.get_numeric_columns()
    variable_index = 0
    for i in range(num_rows):
      for j in range(num_cols):
        if variable_index < len(numeric_variables):
          variable = numeric_variables[variable_index]
          self.dataset[variable].plot(kind='hist', bins=nBins, ax=axs[i, j])
          axs[i, j].set_title(variable)
          variable_index += 1
        else:
          axs[i, j].axis('off')
    plt.tight_layout()
    plt.show()

  def get_categorical_columns(self):
    """Devuelve las columnas categóricas del conjunto de datos."""
    categorical_cols = self.dataset.select_dtypes(include=['object', 'category']).columns
    return categorical_cols

  def plot_bar_charts_categorical_columns(self):
    """
    Genera gráficos de barras para visualizar la distribución de las variables categóricas.
    """
    num_cols = 3
    num_rows = math.ceil(len(self.get_categorical_columns()) / num_cols)
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(12, 4 * num_rows))
    categorical_variables = self.get_categorical_columns()
    variable_index = 0
    for i in range(num_rows):
      for j in range(num_cols):
        if variable_index < len(categorical_variables):
          variable = categorical_variables[variable_index]
          self.dataset[variable].value_counts().plot(kind='bar', ax=axs[i, j])
          axs[i, j].set_title(variable)
          variable_index += 1
        else:
          axs[i, j].axis('off')
    plt.tight_layout()
    plt.show()

  def getCorrelationMatrix(self) -> None:
    """
    Genera y muestra la matriz de correlación entre variables.
    Utiliza un mapa de calor para visualizar la intensidad de la correlación.
    """
    correlation_matrix = self.dataset.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Correlation Matrix")
    plt.show()
  
  def getAutomaticStatisticalEDA(self) -> None:
    """
    Realiza un análisis estadístico automático utilizando la biblioteca Sweetviz.
    Se genera un informe estadístico interactivo.
    """
    try:
      import sweetviz as sv
    except ImportError:
      print("Sweetviz no está instalado. Intentando instalarlo...")
      try:
        import subprocess
        subprocess.run(["pip", "install", "sweetviz"])
        from sweetviz import sv
      except Exception as e:
        print(f"No se pudo instalar Sweetviz. Por favor, instálalo manualmente. Error: {e}")
        return
    advert_report = sv.analyze(self.dataset)
    advert_report.show_notebook(w=1500, h=1000, scale=0.8)

  def getAutomaticGraphicalEDA(self) -> None:
    """
    Realiza un análisis gráfico automático utilizando la biblioteca AutoViz.
    Se generan visualizaciones gráficas automáticas.
    """
    try:
      from autoviz.AutoViz_Class import AutoViz_Class
    except ImportError:
      print("Autoviz no está instalado. Intentando instalarlo...")
      try:
        import subprocess
        subprocess.run(["pip", "install", "autoviz"])
        from autoviz.AutoViz_Class import AutoViz_Class
      except Exception as e:
        print(f"No se pudo instalar Autoviz. Por favor, instálalo manualmente. Error: {e}")
        return
    csv_filename = 'temp_dataset.csv'
    self.dataset.to_csv(csv_filename, index=False)
    AV = AutoViz_Class()
    dft = AV.AutoViz(csv_filename)

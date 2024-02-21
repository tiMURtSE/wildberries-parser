from openpyxl.cell.cell import Cell

class Product:
    ID_COL_INDEX = 0
    ARTICLE_COL_INDEX = 9
    SERIES_COL_IDNEX = 28

    def __init__(self, row: tuple[Cell]):
        self._row = row

        self._id = self._row[self.ID_COL_INDEX].value
        self._article = self._row[self.ARTICLE_COL_INDEX].value
        self._series = self._row[self.SERIES_COL_IDNEX].value
        self._reviews = []

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, value):
        self._reviews = value

    def get_name(self):
        return f"{self._series} {self._article}"

    def show_info(self):
        return {
            "id": self._id,
            "article": self._article,
            "series": self._series,
            "reviews": self._reviews
        }

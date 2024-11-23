from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class Contenido(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, titulo=None, descripcion=None, genero=None, duracion=None, ao_lanzamiento=None, rating=None, url_video=None, thumbnail=None):  # noqa: E501
        """Contenido - a model defined in OpenAPI

        :param id: The id of this Contenido.  # noqa: E501
        :type id: int
        :param titulo: The titulo of this Contenido.  # noqa: E501
        :type titulo: str
        :param descripcion: The descripcion of this Contenido.  # noqa: E501
        :type descripcion: str
        :param genero: The genero of this Contenido.  # noqa: E501
        :type genero: str
        :param duracion: The duracion of this Contenido.  # noqa: E501
        :type duracion: int
        :param ao_lanzamiento: The ao_lanzamiento of this Contenido.  # noqa: E501
        :type ao_lanzamiento: int
        :param rating: The rating of this Contenido.  # noqa: E501
        :type rating: float
        :param url_video: The url_video of this Contenido.  # noqa: E501
        :type url_video: str
        :param thumbnail: The thumbnail of this Contenido.  # noqa: E501
        :type thumbnail: str
        """
        self.openapi_types = {
            'id': int,
            'titulo': str,
            'descripcion': str,
            'genero': str,
            'duracion': int,
            'ao_lanzamiento': int,
            'rating': float,
            'url_video': str,
            'thumbnail': str
        }

        self.attribute_map = {
            'id': 'id',
            'titulo': 'titulo',
            'descripcion': 'descripcion',
            'genero': 'genero',
            'duracion': 'duracion',
            'ao_lanzamiento': 'añoLanzamiento',
            'rating': 'rating',
            'url_video': 'urlVideo',
            'thumbnail': 'thumbnail'
        }

        self._id = id
        self._titulo = titulo
        self._descripcion = descripcion
        self._genero = genero
        self._duracion = duracion
        self._ao_lanzamiento = ao_lanzamiento
        self._rating = rating
        self._url_video = url_video
        self._thumbnail = thumbnail

    @classmethod
    def from_dict(cls, dikt) -> 'Contenido':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Contenido of this Contenido.  # noqa: E501
        :rtype: Contenido
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Contenido.


        :return: The id of this Contenido.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Contenido.


        :param id: The id of this Contenido.
        :type id: int
        """

        self._id = id

    @property
    def titulo(self) -> str:
        """Gets the titulo of this Contenido.


        :return: The titulo of this Contenido.
        :rtype: str
        """
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str):
        """Sets the titulo of this Contenido.


        :param titulo: The titulo of this Contenido.
        :type titulo: str
        """

        self._titulo = titulo

    @property
    def descripcion(self) -> str:
        """Gets the descripcion of this Contenido.


        :return: The descripcion of this Contenido.
        :rtype: str
        """
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion: str):
        """Sets the descripcion of this Contenido.


        :param descripcion: The descripcion of this Contenido.
        :type descripcion: str
        """

        self._descripcion = descripcion

    @property
    def genero(self) -> str:
        """Gets the genero of this Contenido.


        :return: The genero of this Contenido.
        :rtype: str
        """
        return self._genero

    @genero.setter
    def genero(self, genero: str):
        """Sets the genero of this Contenido.


        :param genero: The genero of this Contenido.
        :type genero: str
        """

        self._genero = genero

    @property
    def duracion(self) -> int:
        """Gets the duracion of this Contenido.


        :return: The duracion of this Contenido.
        :rtype: int
        """
        return self._duracion

    @duracion.setter
    def duracion(self, duracion: int):
        """Sets the duracion of this Contenido.


        :param duracion: The duracion of this Contenido.
        :type duracion: int
        """

        self._duracion = duracion

    @property
    def ao_lanzamiento(self) -> int:
        """Gets the ao_lanzamiento of this Contenido.


        :return: The ao_lanzamiento of this Contenido.
        :rtype: int
        """
        return self._ao_lanzamiento

    @ao_lanzamiento.setter
    def ao_lanzamiento(self, ao_lanzamiento: int):
        """Sets the ao_lanzamiento of this Contenido.


        :param ao_lanzamiento: The ao_lanzamiento of this Contenido.
        :type ao_lanzamiento: int
        """

        self._ao_lanzamiento = ao_lanzamiento

    @property
    def rating(self) -> float:
        """Gets the rating of this Contenido.


        :return: The rating of this Contenido.
        :rtype: float
        """
        return self._rating

    @rating.setter
    def rating(self, rating: float):
        """Sets the rating of this Contenido.


        :param rating: The rating of this Contenido.
        :type rating: float
        """

        self._rating = rating

    @property
    def url_video(self) -> str:
        """Gets the url_video of this Contenido.


        :return: The url_video of this Contenido.
        :rtype: str
        """
        return self._url_video

    @url_video.setter
    def url_video(self, url_video: str):
        """Sets the url_video of this Contenido.


        :param url_video: The url_video of this Contenido.
        :type url_video: str
        """

        self._url_video = url_video

    @property
    def thumbnail(self) -> str:
        """Gets the thumbnail of this Contenido.


        :return: The thumbnail of this Contenido.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail: str):
        """Sets the thumbnail of this Contenido.


        :param thumbnail: The thumbnail of this Contenido.
        :type thumbnail: str
        """

        self._thumbnail = thumbnail

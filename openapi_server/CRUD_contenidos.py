from sqlalchemy.orm import Session
from sqlalchemy import desc
from openapi_server.databaseContenido import Contenido as ContenidoDB

def obtener_contenido_por_id(db: Session, contenido_id: int):
    try:
        contenido = db.query(ContenidoDB).filter(ContenidoDB.id_contenido == contenido_id).first()
        if contenido:
            return contenido
        else:
            return None
    except Exception as e:
        # Agregar lógica de manejo de excepciones
        print(f"Error al obtener contenido por ID {contenido_id}: {e}")
        raise

def obtener_catalogo(db: Session, genero: str = None, orden: str = None):
    try:
        query = db.query(ContenidoDB)
        if genero:
            query = query.filter(ContenidoDB.genero.ilike(f'%{genero}%'))
        if orden:
            if orden.lower() == 'popularidad':
                query = query.order_by(desc(ContenidoDB.rating))
            elif orden.lower() == 'fecha':
                query = query.order_by(desc(ContenidoDB.año_lanzamiento))
        contenidos_db = query.all()
        contenidos_list = [contenido.to_dict() for contenido in contenidos_db]
        return contenidos_list
    except Exception as e:
        # Agregar lógica de manejo de excepciones
        print(f"Error al obtener catálogo: {e}")
        raise

def reproducir_contenido(db: Session, contenido_id: int):
    try:
        contenido = db.query(ContenidoDB).filter(ContenidoDB.id_contenido == contenido_id).first()
        if contenido:
            return contenido
        else:
            return None
    except Exception as e:
        # Agregar lógica de manejo de excepciones
        print(f"Error al reproducir contenido ID {contenido_id}: {e}")
        raise

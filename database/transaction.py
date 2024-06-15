from contextlib import contextmanager
from sqlalchemy import exc
from functools import wraps
from retry import retry


from database.db import BaseSession


@contextmanager
def transaction_manager():
    try:
        db = BaseSession()
        yield db

        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        db.close() 



def transaction(func):
    @wraps(func)
    @retry((exc.OperationalError, exc.IntegrityError), delay=5, tries=5)
    def decorator(*args, **kwargs):
        
        try:
            with transaction_manager() as db:
                params = list(args)
                params.insert(1, db) if params else params.append(db)
                params = tuple(params)

                return func(*params, **kwargs)

        except (exc.IntegrityError) as e:  # Deadlock
            raise e

        except exc.SQLAlchemyError as e:
            raise
        
    return decorator

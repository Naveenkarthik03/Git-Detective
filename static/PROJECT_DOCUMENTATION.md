# Repository Documentation

Repository Name: Analyzed Repository

Total Python Files: 16

## Project Structure

### models.py
- Path: temp_repo/backend/app/models.py
- Lines of Code: 129
- Imports:
  - import uuid
  - from datetime import datetime, timezone
  - from pydantic import EmailStr
  - from sqlalchemy import DateTime
  - from sqlmodel import Field, Relationship, SQLModel

### backend_pre_start.py
- Path: temp_repo/backend/app/backend_pre_start.py
- Lines of Code: 39
- Imports:
  - import logging
  - from sqlalchemy import Engine
  - from sqlmodel import Session, select
  - from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed
  - from app.core.db import engine

### initial_data.py
- Path: temp_repo/backend/app/initial_data.py
- Lines of Code: 23
- Imports:
  - import logging
  - from sqlmodel import Session
  - from app.core.db import engine, init_db

### utils.py
- Path: temp_repo/backend/app/utils.py
- Lines of Code: 123
- Imports:
  - import logging
  - from dataclasses import dataclass
  - from datetime import datetime, timedelta, timezone
  - from pathlib import Path
  - from typing import Any
  - import emails  # type: ignore[import-untyped]
  - import jwt
  - from jinja2 import Template
  - from jwt.exceptions import InvalidTokenError
  - from app.core import security
  - from app.core.config import settings

### main.py
- Path: temp_repo/backend/app/main.py
- Lines of Code: 33
- Imports:
  - import sentry_sdk
  - from fastapi import FastAPI
  - from fastapi.routing import APIRoute
  - from starlette.middleware.cors import CORSMiddleware
  - from app.api.main import api_router
  - from app.core.config import settings

### crud.py
- Path: temp_repo/backend/app/crud.py
- Lines of Code: 68
- Imports:
  - import uuid
  - from typing import Any
  - from sqlmodel import Session, select
  - from app.core.security import get_password_hash, verify_password
  - from app.models import Item, ItemCreate, User, UserCreate, UserUpdate

### db.py
- Path: temp_repo/backend/app/core/db.py
- Lines of Code: 33
- Imports:
  - from sqlmodel import Session, create_engine, select
  - from app import crud
  - from app.core.config import settings
  - from app.models import User, UserCreate

### config.py
- Path: temp_repo/backend/app/core/config.py
- Lines of Code: 119
- Imports:
  - import secrets
  - import warnings
  - from typing import Annotated, Any, Literal
  - from pydantic import (
  - from pydantic_settings import BaseSettings, SettingsConfigDict
  - from typing_extensions import Self

### security.py
- Path: temp_repo/backend/app/core/security.py
- Lines of Code: 36
- Imports:
  - from datetime import datetime, timedelta, timezone
  - from typing import Any
  - import jwt
  - from pwdlib import PasswordHash
  - from pwdlib.hashers.argon2 import Argon2Hasher
  - from pwdlib.hashers.bcrypt import BcryptHasher
  - from app.core.config import settings

### deps.py
- Path: temp_repo/backend/app/api/deps.py
- Lines of Code: 57
- Imports:
  - from collections.abc import Generator
  - from typing import Annotated
  - import jwt
  - from fastapi import Depends, HTTPException, status
  - from fastapi.security import OAuth2PasswordBearer
  - from jwt.exceptions import InvalidTokenError
  - from pydantic import ValidationError
  - from sqlmodel import Session
  - from app.core import security
  - from app.core.config import settings
  - from app.core.db import engine
  - from app.models import TokenPayload, User

### main.py
- Path: temp_repo/backend/app/api/main.py
- Lines of Code: 14
- Imports:
  - from fastapi import APIRouter
  - from app.api.routes import items, login, private, users, utils
  - from app.core.config import settings

### users.py
- Path: temp_repo/backend/app/api/routes/users.py
- Lines of Code: 232
- Imports:
  - import uuid
  - from typing import Any
  - from fastapi import APIRouter, Depends, HTTPException
  - from sqlmodel import col, delete, func, select
  - from app import crud
  - from app.api.deps import (
  - from app.core.config import settings
  - from app.core.security import get_password_hash, verify_password
  - from app.models import (
  - from app.utils import generate_new_account_email, send_email

### utils.py
- Path: temp_repo/backend/app/api/routes/utils.py
- Lines of Code: 31
- Imports:
  - from fastapi import APIRouter, Depends
  - from pydantic.networks import EmailStr
  - from app.api.deps import get_current_active_superuser
  - from app.models import Message
  - from app.utils import generate_test_email, send_email

### login.py
- Path: temp_repo/backend/app/api/routes/login.py
- Lines of Code: 123
- Imports:
  - from datetime import timedelta
  - from typing import Annotated, Any
  - from fastapi import APIRouter, Depends, HTTPException
  - from fastapi.responses import HTMLResponse
  - from fastapi.security import OAuth2PasswordRequestForm
  - from app import crud
  - from app.api.deps import CurrentUser, SessionDep, get_current_active_superuser
  - from app.core import security
  - from app.core.config import settings
  - from app.models import Message, NewPassword, Token, UserPublic, UserUpdate
  - from app.utils import (

### items.py
- Path: temp_repo/backend/app/api/routes/items.py
- Lines of Code: 113
- Imports:
  - import uuid
  - from typing import Any
  - from fastapi import APIRouter, HTTPException
  - from sqlmodel import col, func, select
  - from app.api.deps import CurrentUser, SessionDep
  - from app.models import Item, ItemCreate, ItemPublic, ItemsPublic, ItemUpdate, Message

### private.py
- Path: temp_repo/backend/app/api/routes/private.py
- Lines of Code: 38
- Imports:
  - from typing import Any
  - from fastapi import APIRouter
  - from pydantic import BaseModel
  - from app.api.deps import SessionDep
  - from app.core.security import get_password_hash
  - from app.models import (


## Workflow


GitHub URL

↓

Clone Repository

↓

Scan Files

↓

Dependency Graph

↓

AI Analysis

↓

Architecture Diagram

↓

Documentation Generation


## Generated By

Git-Detective
Generated At: 18 Jun 2026, 02:52 PM
from datetime import datetime

from sqlalchemy import (
    create_engine,
    String,
    Integer,
    Float,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker,
    relationship
)

from .config import DATABASE_URL


connect_args = {}

if DATABASE_URL.startswith("sqlite"):
    connect_args = {
        "check_same_thread": False
    }


engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    user_id: Mapped[str] = mapped_column(
        String(80),
        unique=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(120)
    )

    age: Mapped[int] = mapped_column(
        Integer
    )

    weight: Mapped[float] = mapped_column(
        Float
    )

    goal: Mapped[str] = mapped_column(
        String(80)
    )

    intensity: Mapped[str] = mapped_column(
        String(20)
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    plans: Mapped[list["Plan"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )


class Plan(Base):
    __tablename__ = "plans"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.user_id"),
        index=True
    )

    original_plan: Mapped[str] = mapped_column(
        Text
    )

    updated_plan: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    feedback: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    nutrition_tip: Mapped[str] = mapped_column(
        Text
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    user: Mapped["User"] = relationship(
        back_populates="plans"
    )


def init_db():
    Base.metadata.create_all(
        bind=engine
    )


def save_user(data: dict):
    db = SessionLocal()

    try:
        user = (
            db.query(User)
            .filter_by(
                user_id=data["user_id"]
            )
            .first()
        )

        if user:
            for key, value in data.items():
                setattr(user, key, value)

        else:
            user = User(**data)
            db.add(user)

        db.commit()
        db.refresh(user)

        return user

    finally:
        db.close()


def save_plan(
    user_id: str,
    original_plan: str,
    nutrition_tip: str
):
    db = SessionLocal()

    try:
        plan = Plan(
            user_id=user_id,
            original_plan=original_plan,
            nutrition_tip=nutrition_tip
        )

        db.add(plan)

        db.commit()

        db.refresh(plan)

        return plan

    finally:
        db.close()


def get_plan(user_id: str):
    db = SessionLocal()

    try:
        return (
            db.query(Plan)
            .filter_by(user_id=user_id)
            .order_by(Plan.id.desc())
            .first()
        )

    finally:
        db.close()


def update_plan(
    user_id: str,
    updated_plan: str,
    feedback: str,
    nutrition_tip: str | None = None
):
    db = SessionLocal()

    try:
        plan = (
            db.query(Plan)
            .filter_by(user_id=user_id)
            .order_by(Plan.id.desc())
            .first()
        )

        if not plan:
            return None

        plan.updated_plan = updated_plan
        plan.feedback = feedback

        if nutrition_tip:
            plan.nutrition_tip = nutrition_tip

        db.commit()
        db.refresh(plan)

        return plan

    finally:
        db.close()


def get_all_users():
    db = SessionLocal()

    try:
        return (
            db.query(User)
            .order_by(User.created_at.desc())
            .all()
        )

    finally:
        db.close()


def get_user_with_plan(user_id: str):
    db = SessionLocal()

    try:
        user = (
            db.query(User)
            .filter_by(user_id=user_id)
            .first()
        )

        plan = (
            db.query(Plan)
            .filter_by(user_id=user_id)
            .order_by(Plan.id.desc())
            .first()
        )

        return user, plan

    finally:
        db.close()


def delete_user(user_id: str):
    db = SessionLocal()

    try:
        user = (
            db.query(User)
            .filter_by(user_id=user_id)
            .first()
        )

        if user:
            db.delete(user)
            db.commit()
            return True

        return False

    finally:
        db.close()
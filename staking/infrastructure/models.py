from sqlalchemy import Column, Integer
from sqlalchemy.dialects.mysql import JSON, TIMESTAMP, VARCHAR, BOOLEAN, BIGINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import func

Base = declarative_base()


class StakeWindow(Base):
    __tablename__ = "stake_window"
    id = Column("id", Integer, primary_key=True)
    blockchain_id = Column("blockchain_id", Integer, nullable=False)
    start_period = Column("start_period", Integer, nullable=False)
    submission_end_period = Column("submission_end_period", Integer, nullable=False)
    approval_end_period = Column("approval_end_period", Integer, nullable=False)
    request_withdraw_start_period = Column("request_withdraw_start_period", Integer, nullable=False)
    end_period = Column("end_period", Integer, nullable=False)
    min_stake = Column("min_stake", BIGINT, nullable=False)
    max_stake = Column("max_stake", BIGINT, nullable=False)
    window_max_cap = Column("window_max_cap", BIGINT, nullable=False)
    open_for_external = Column("open_for_external", BOOLEAN, nullable=False)
    total_stake = Column("total_stake", BIGINT, nullable=False)
    reward_amount = Column("reward_amount", BIGINT, nullable=False)
    token_operator = Column("token_operator", VARCHAR(50), nullable=False)
    created_on = Column("created_on", TIMESTAMP(timezone=False), nullable=False)
    updated_on = Column("updated_on", TIMESTAMP(timezone=False), nullable=False, default=func.utc_timestamp())


class StakeHolder(Base):
    __tablename__ = "stake_holder"
    id = Column("id", Integer, primary_key=True)
    blockchain_id = Column("blockchain_id", Integer, nullable=False)
    staker = Column("staker", VARCHAR(50), nullable=False)
    # amount = Column("amount", BIGINT, nullable=False) no more needed
    # amount_staked = Column("amount_staked", BIGINT, nullable=False) no more needed
    amount_pending_for_approval = Column("amount_pending_for_approval", BIGINT, nullable=False)
    amount_approved = Column("amount_approved", BIGINT, nullable=False)
    auto_renewal = Column("auto_renewal", BOOLEAN, nullable=False)
    # status = Column("status", Integer, nullable=False) status will be based on amount_approved and amount_pending_for_approval
    # staker_id = Column("staker_id", Integer, nullable=False) no more needed
    block_no_created = Column("block_no_created", Integer, nullable=False)
    created_on = Column("created_on", TIMESTAMP(timezone=False), nullable=False)
    updated_on = Column("updated_on", TIMESTAMP(timezone=False), nullable=False, default=func.utc_timestamp())


class StakeTransaction(Base):
    __tablename__ = "stake_transaction"
    transaction_id = Column("transaction_id", VARCHAR(128), primary_key=True, nullable=False)
    blockchain_id = Column("blockchain_id", Integer, nullable=False)
    staker = Column("staker", VARCHAR(50))
    event = Column("event", VARCHAR(128), nullable=False)
    event_data = Column("event_data", JSON, nullable=False)
    block_no = Column("block_no", Integer, nullable=False)
    transaction_hash = Column("transaction_hash", VARCHAR(128), nullable=False)
    created_on = Column("created_on", TIMESTAMP(timezone=False), nullable=False)
    updated_on = Column("updated_on", TIMESTAMP(timezone=False), nullable=False, default=func.utc_timestamp())
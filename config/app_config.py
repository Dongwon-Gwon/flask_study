import os


class LocalLevelConfig:
    ENV = "development"
    DEBUG = True


class ProductionLevelConfig:
    ENV = "production"
    DEBUG = False
    

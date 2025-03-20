from abc import ABC, abstractmethod

import allure
from playwright.sync_api import Locator, Page, expect

class Component(ABC):

    def __init__(self, page: Page, locator: str, name: str) -> None:
        self.page = page
        self.name = name
        self.locator = locator

    @property
    @abstractmethod
    def type_of(self) -> str:
        return 'component'
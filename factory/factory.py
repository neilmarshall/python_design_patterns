from abc import ABC, abstractmethod

# abstract product interface - specifies interface that concrete products must implement
class Section(ABC):
    @abstractmethod
    def describe(self):
        pass


# concrete product - implements abstract product interface
class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


# concrete product - implements abstract product interface
class AlbumSection(Section):
    def describe(self):
        print("Album Section")


# concrete product - implements abstract product interface
class PatentSection(Section):
    def describe(self):
        print("Patent Section")


# concrete product - implements abstract product interface
class PublicationSection(Section):
    def describe(self):
        print("Publication Section")


# abstract creator - specifies interface that concrete creators must implement
class Profile(ABC):
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        self.sections.append(section)


# concrete creator - implements abstract creator interface
class LinkedIn(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(PatentSection())
        self.add_sections(PublicationSection())


# concrete creator - implements abstract creator interface
class Facebook(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())


if __name__ == '__main__':
    profile_type = input("Which Profile would you like to create - LinkedIn or Facebook?")
    profile = eval(profile_type)()
    print("Creating Profile...", type(profile).__name__)
    print("Profile has sections --", profile.get_sections())
    for section in profile.get_sections():
        section.describe()
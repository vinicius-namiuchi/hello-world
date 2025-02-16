class Dog():
    """Uma tentiva simples de modelar um cachorro."""

    def __init__(self, name, age):
        """Inicializa os atributos name e age."""
        self.name = name
        self.age = age

    def sit(self):
        """Simula um cachorro sentando em resposta a um comando."""
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando."""
        print(self.name.title()+" rolled over!")

my_dog = Dog("Pipoca", 13)
your_dog = Dog("Peperoni", 14)

print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()

print("\nYour dog's name is "+your_dog.name.title()+".")
print("Your dog is "+str(your_dog.age)+" years old.")
your_dog.sit()
class Animal {
    void fazerSom(){
        System.out.println("Fazendo som genérico");
    }
}

class Cachorro extends Animal{
    @Override

    void fazerSom(){
        System.out.println("AuAU");
    }
}

public class Heranca {
    public static void main(String[] args) throws Exception {
        //Cria a instância do cachorro

        Cachorro meuCachorro = new Cachorro();

        meuCachorro.fazerSom();

        //Cria a instância gato
        
        Animal gato = new Animal();

        gato.fazerSom();
    }
}

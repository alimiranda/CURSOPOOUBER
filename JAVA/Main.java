class Main {

    public static void main(String[] args) {
        System.out.println("Hola Mundo");

        Car car = new Car("AMQ123", new Account("Andrés Herrera", "10349586"));

        car.passengers = 4;
        car.printDataCar();

        Car car2 = new Car("QWE123", new Account("Gloria Zapata", "473059"));

        car2.printDataCar();

    }
}

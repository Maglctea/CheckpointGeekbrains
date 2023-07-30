import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        ToyStore toyStore = new ToyStore();
        toyStore.addToy(1, "Плюшевый медведь", 10, 30);
        toyStore.addToy(2, "Машинка", 15, 20);
        toyStore.addToy(3, "Кукла", 12, 25);
        toyStore.addToy(4, "Конструктор", 8, 25);

        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите количество призов для розыгрыша:");
        int numPrizes = scanner.nextInt();

        List<Toy> prizes = new ArrayList<>();
        for (int i = 0; i < numPrizes; i++) {
            Toy prize = toyStore.selectToy();
            prizes.add(prize);
        }

        System.out.println("В качестве призов были выбраны следующие игрушки:");
        for (Toy prize : prizes) {
            System.out.println(prize.getName());
            toyStore.writePrizeToyToFile(prize, "prize_toys.txt");
        }

        System.out.println("Инвентарь магазина игрушек после выбора приза:");
        for (Toy toy : toyStore.toys) {
            System.out.println(toy.getName() + ": " + toy.getQuantity());
        }
    }
}

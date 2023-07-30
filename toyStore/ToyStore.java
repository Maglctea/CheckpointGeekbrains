import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class ToyStore {
    List<Toy> toys = new ArrayList<>();

    public void addToy(int id, String name, int quantity, int weight) {
        Toy toy = new Toy(id, name, quantity, weight);
        toys.add(toy);
    }

    public void changeWeight(int id, int weight) {
        for (Toy toy : toys) {
            if (toy.getId() == id) {
                toy.setWeight(weight);
                break;
            }
        }
    }

    public Toy selectToy() {
        Random random = new Random();
        int totalWeight = 0;
        for (Toy toy : toys) {
            totalWeight += toy.getWeight();
        }
        int selectedWeight = random.nextInt(totalWeight);
        int currentWeight = 0;
        for (Toy toy : toys) {
            currentWeight += toy.getWeight();
            if (selectedWeight < currentWeight) {
                toy.setQuantity(toy.getQuantity() - 1);
                return toy;
            }
        }
        return null;
    }

    public void writePrizeToyToFile(Toy toy, String filename) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter(filename, true));
        writer.write(toy.getId() + "," + toy.getName() + "\n");
        writer.close();
    }

}
// Rectangle class to represent a rectangle shape
class Rectangle {
    // Properties (attributes)
    private double length;
    private double width;

    // Constructor to initialize length and width
    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    // Method to calculate area of the rectangle
    public double calculateArea() {
        return length * width;
    }

    // Method to calculate perimeter of the rectangle
    public double calculatePerimeter() {
        return 2 * (length + width);
    }

    // Optional: Getter methods (good practice for encapsulation)
    public double getLength() {
        return length;
    }

    public double getWidth() {
        return width;
    }
}

// Main class to test the Rectangle class
public class Main {
    public static void main(String[] args) {

        // Creating first Rectangle object
        Rectangle rect1 = new Rectangle(5.0, 3.0);

        // Creating second Rectangle object
        Rectangle rect2 = new Rectangle(7.5, 4.2);

        // Calculating and printing results for first rectangle
        System.out.println("Rectangle 1:");
        System.out.println("Length: " + rect1.getLength());
        System.out.println("Width: " + rect1.getWidth());
        System.out.println("Area: " + rect1.calculateArea());
        System.out.println("Perimeter: " + rect1.calculatePerimeter());

        System.out.println(); // Blank line for readability

        // Calculating and printing results for second rectangle
        System.out.println("Rectangle 2:");
        System.out.println("Length: " + rect2.getLength());
        System.out.println("Width: " + rect2.getWidth());
        System.out.println("Area: " + rect2.calculateArea());
        System.out.println("Perimeter: " + rect2.calculatePerimeter());
    }
}
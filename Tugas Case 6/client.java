import java.rmi.Naming;

public class Client {
    public static void main(String[] args) {
        try {
            // 7. Cari obyek di RMI Registry server
            // (Stub akan di-download secara otomatis)
            Calculator calc = (Calculator) Naming.lookup("rmi://localhost:1099/CalculatorService");
            
            // 8. Panggil metode seolah-olah obyek ada di lokal
            int hasilTambah = calc.add(25, 10);
            int hasilKurang = calc.subtract(50, 5);
            
            System.out.println("Klien: Hasil 25 + 10 = " + hasilTambah);
            System.out.println("Klien: Hasil 50 - 5 = " + hasilKurang);
            
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
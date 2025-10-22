import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class Server {
    public static void main(String[] args) {
        try {
            // 4. Buat RMI Registry di port 1099
            LocateRegistry.createRegistry(1099);
            
            // 5. Buat obyek implementasi
            Calculator calc = new CalculatorImpl();
            
            // 6. Daftarkan (bind) obyek ke RMI Registry dengan nama "CalculatorService"
            Naming.rebind("rmi://localhost:1099/CalculatorService", calc);
            
            System.out.println("Server Kalkulator siap...");
            
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
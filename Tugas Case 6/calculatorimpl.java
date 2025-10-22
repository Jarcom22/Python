import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

// 3. Implementasi harus extend 'UnicastRemoteObject'
public class CalculatorImpl extends UnicastRemoteObject implements Calculator {

    // Konstruktor default yang melempar RemoteException
    public CalculatorImpl() throws RemoteException {
        super();
    }

    // Implementasi logika metode
    @Override
    public int add(int a, int b) throws RemoteException {
        System.out.println("Server: Menerima permintaan add(" + a + ", " + b + ")");
        return a + b;
    }

    @Override
    public int subtract(int a, int b) throws RemoteException {
        System.out.println("Server: Menerima permintaan subtract(" + a + ", " + b + ")");
        return a - b;
    }
}
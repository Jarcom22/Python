import java.rmi.Remote;
import java.rmi.RemoteException;

// 1. Interface harus 'public' dan extend 'java.rmi.Remote'
public interface Calculator extends Remote {
    
    // 2. Setiap metode harus melempar 'RemoteException'
    int add(int a, int b) throws RemoteException;
    int subtract(int a, int b) throws RemoteException;
}
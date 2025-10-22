import javax.crypto.*;
import javax.crypto.spec.*;
import java.io.*;
import java.security.*;
import java.util.Scanner;

public class HW6 {
    private static final String ALGORITHM = "AES/CBC/PKCS5Padding";
    private static final String KEY_ALGORITHM = "PBKDF2WithHmacSHA256";
    private static final int KEY_SIZE = 256;
    private static final int ITERATION_COUNT = 65536;
    private static final int IV_SIZE = 16;
    
    // Fixed salt for consistency between encryption and decryption
    private static final byte[] SALT = "HW6SaltValue1234".getBytes();

    public static void main(String[] args) {
        if (args.length != 3) {
            System.out.println("Usage: java HW6 <encrypt|decrypt> <inputFile> <outputFile>");
            return;
        }

        String mode = args[0].toLowerCase();
        String inputFile = args[1];
        String outputFile = args[2];

        // Prompt for password
        System.out.print("Enter password: ");
        Scanner scanner = new Scanner(System.in);
        String password = scanner.nextLine();

        try {
            if (mode.equals("encrypt")) {
                encryptFile(inputFile, outputFile, password);
                System.out.println("File encrypted successfully!");
            } else if (mode.equals("decrypt")) {
                decryptFile(inputFile, outputFile, password);
                System.out.println("File decrypted successfully!");
            } else {
                System.out.println("Invalid mode. Use 'encrypt' or 'decrypt'");
            }
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
        }
    }

    private static SecretKey generateKey(String password) throws Exception {
        SecretKeyFactory factory = SecretKeyFactory.getInstance(KEY_ALGORITHM);
        KeySpec spec = new PBEKeySpec(password.toCharArray(), SALT, ITERATION_COUNT, KEY_SIZE);
        SecretKey tmp = factory.generateSecret(spec);
        return new SecretKeySpec(tmp.getEncoded(), "AES");
    }

    private static void encryptFile(String inputFile, String outputFile, String password) throws Exception {
        // Generate key from password
        SecretKey key = generateKey(password);
        
        // Generate random IV
        byte[] iv = new byte[IV_SIZE];
        SecureRandom random = new SecureRandom();
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);
        
        // Initialize cipher
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);
        
        // Read input file
        FileInputStream fis = new FileInputStream(inputFile);
        byte[] inputBytes = fis.readAllBytes();
        fis.close();
        
        // Encrypt
        byte[] encryptedBytes = cipher.doFinal(inputBytes);
        
        // Write IV followed by encrypted data
        FileOutputStream fos = new FileOutputStream(outputFile);
        fos.write(iv); // Write IV as first 16 bytes
        fos.write(encryptedBytes);
        fos.close();
    }

    private static void decryptFile(String inputFile, String outputFile, String password) throws Exception {
        // Generate key from password
        SecretKey key = generateKey(password);
        
        // Read encrypted file
        FileInputStream fis = new FileInputStream(inputFile);
        byte[] fileContent = fis.readAllBytes();
        fis.close();
        
        // Extract IV from first 16 bytes
        byte[] iv = new byte[IV_SIZE];
        System.arraycopy(fileContent, 0, iv, 0, IV_SIZE);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);
        
        // Extract encrypted data (everything after IV)
        byte[] encryptedBytes = new byte[fileContent.length - IV_SIZE];
        System.arraycopy(fileContent, IV_SIZE, encryptedBytes, 0, encryptedBytes.length);
        
        // Initialize cipher for decryption
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.DECRYPT_MODE, key, ivSpec);
        
        // Decrypt
        byte[] decryptedBytes = cipher.doFinal(encryptedBytes);
        
        // Write decrypted data
        FileOutputStream fos = new FileOutputStream(outputFile);
        fos.write(decryptedBytes);
        fos.close();
    }
}
import java.io.*;
import java.util.Scanner;
import java.nio.file.Paths;
import java.nio.file.Files;

import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.spec.KeySpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.IvParameterSpec;
import java.security.SecureRandom;
import java.util.Arrays;
import java.util.Base64;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.CipherOutputStream;
import javax.crypto.CipherInputStream;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.nio.CharBuffer;


public class HW6 {
	private static final String salt = "0123456789ABCDEF";
	
	private static SecretKey getKeyFromPassword(String password, String salt) throws Exception {
		SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
		KeySpec spec = new PBEKeySpec(password.toCharArray(), salt.getBytes(), 65536, 256);
		SecretKey secret = new SecretKeySpec(factory.generateSecret(spec).getEncoded(), "AES");
		return secret;
	}

	public static void encrypt(String pw, String in, String out) throws Exception {
		SecureRandom r = new SecureRandom();
		
		// Create key from password and salt
		SecretKey key = getKeyFromPassword(pw, salt);
		
		// Create Initialization Vector
		byte[] iv = new byte[16];
		r.nextBytes(iv);
		IvParameterSpec ivSpec = new IvParameterSpec(iv);

 		// Create cipher
		Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
		cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);

		// Establish file streams
		FileInputStream inputStream = new FileInputStream(in);
		FileOutputStream outputStream = new FileOutputStream(out);

		// Write the initialization vector to the output stream
		// Don't use the cipher stream because you don't want it encrypted
		outputStream.write(iv);

		// Create cipher output stream
		CipherOutputStream cipherOutputStream = new CipherOutputStream(outputStream, cipher);

		// Read from cleartext stream and write to the cipher stream
		// Writing to the cipher stream will encrypt the data being written
		byte[] buffer = new byte[4096];
		int bytesRead;
		while ((bytesRead = inputStream.read(buffer)) != -1) {
			cipherOutputStream.write(buffer, 0, bytesRead);
		}
		
		// Flush and close streams
		cipherOutputStream.flush();
		cipherOutputStream.close();
		inputStream.close();
	}
	

	public static void decrypt(String pw, String in, String out) throws Exception {
		
		// Establish input file stream
		FileInputStream inputStream = new FileInputStream(in);
		
		// Create key from password and salt
		SecretKey key = getKeyFromPassword(pw, salt);

		// Read the initialization vector from the encrypted file
		byte[] iv = new byte[16];
		inputStream.read(iv);
		IvParameterSpec ivSpec = new IvParameterSpec(iv);

		// Create cipher and cipher stream
		Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
		cipher.init(Cipher.DECRYPT_MODE, key, ivSpec);
		
		// Create cipher input stream
		CipherInputStream cipherInputStream = new CipherInputStream(inputStream, cipher);

		// Establish output stream
		FileOutputStream outputStream = new FileOutputStream(out);

		// Read from cipher stream and write to the output stream
		// Reading from the cipher stream will decrypt the data being read
		byte[] buffer = new byte[4096];
		int bytesRead;
		while ((bytesRead = cipherInputStream.read(buffer)) != -1) {
			outputStream.write(buffer, 0, bytesRead);
		}
		
		// Flush and close streams
		outputStream.flush();
		outputStream.close();
		cipherInputStream.close();
	}

    public static void main(String args[]) {
		String action = "";
		String inputFilepath = "";
		String outputFilepath = "";
		String password = null;
		
		try {
			if(args.length != 3) {
				System.out.println("Usage: HW6 {encrypt|decrypt} inputFile outputFile");
				throw(new Exception("Missing or invalid arguments"));
			} else {
				action = args[0];
				inputFilepath = args[1];
				outputFilepath = args[2];
				char[] p = System.console().readPassword("Enter password: ");
				password = new String(p);
			}
		
			if(action.equals("encrypt")) {
				encrypt(password, inputFilepath, outputFilepath);
			} else if(action.equals("decrypt")) {
				decrypt(password, inputFilepath, outputFilepath);
			} else {
				throw(new Exception("Invalid action"));
			}
		}
		catch (Exception ex) {
			System.out.println( ex.getMessage() );
			System.exit(1);
		}
	}
}
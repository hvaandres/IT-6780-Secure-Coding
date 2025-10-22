# HW6 - AES File Encryption/Decryption Program

## Author
Andres Haro
October/21/2025

## Overview
This program implements file encryption and decryption using the AES (Advanced Encryption Standard) algorithm in CBC (Cipher Block Chaining) mode with PKCS5Padding. It can encrypt and decrypt both text files and binary files (such as images).

## Features
- **AES-256 Encryption**: Uses AES algorithm with 256-bit keys
- **Password-Based Key Derivation**: Uses PBKDF2WithHmacSHA256 with 65,536 iterations
- **CBC Mode with PKCS5Padding**: Secure block cipher mode
- **Random Initialization Vector (IV)**: Generated for each encryption operation
- **Binary File Support**: Works with any file type (text, images, documents, etc.)

## Technical Implementation

### Encryption Process:
1. Derives a 256-bit AES key from the user password using PBKDF2
2. Generates a random 16-byte Initialization Vector (IV)
3. Initializes AES cipher in CBC mode with PKCS5Padding
4. Writes the IV as the first 16 bytes of the output file (unencrypted)
5. Encrypts the input file and writes encrypted data after the IV

### Decryption Process:
1. Derives the same 256-bit AES key from the user password
2. Reads the first 16 bytes of the encrypted file to retrieve the IV
3. Initializes AES cipher in decrypt mode
4. Decrypts the remaining file content and writes to output file

### Security Features:
- **Salt**: Fixed salt value "0123456789ABCDEF" for key derivation
- **Key Derivation**: PBKDF2 with 65,536 iterations makes brute-force attacks difficult
- **IV Storage**: IV is stored with the encrypted file (not secret, but must be available for decryption)

## Requirements
- Java Development Kit (JDK) 8 or higher
- Java Cryptography Extension (JCE) - included in modern JDK versions

## Compilation
```bash
javac HW6.java
```

## Usage
```bash
java HW6 <encrypt|decrypt> <inputFile> <outputFile>
```

### Parameters:
- `encrypt|decrypt`: Operation mode
- `inputFile`: Path to the file to encrypt/decrypt
- `outputFile`: Path where the result will be saved

## Examples

### Example 1: Encrypt a Text File
```bash
java HW6 encrypt message.txt message.encrypted
Enter password: PASSWORD
```

### Example 2: Decrypt the Encrypted File
```bash
java HW6 decrypt message.encrypted COPY_message.txt
Enter password: PASSWORD
```
**Note**: Use the same password that was used for encryption

### Example 3: Encrypt an Image
```bash
java HW6 encrypt smile.png smile.encrypted
Enter password: mySecurePassword123
```

### Example 4: Decrypt the Image
```bash
java HW6 decrypt smile.encrypted COPY_smile.png
Enter password: mySecurePassword123
```

### Example 5: Decrypt the Riddle (Assignment Requirement)
```bash
java HW6 decrypt riddle.encrypted riddle.png
Enter password: IT6780
```

## Important Notes

1. **Password Consistency**: You must use the EXACT same password for decryption that was used for encryption
2. **Case Sensitivity**: Passwords are case-sensitive
3. **File Overwriting**: The program will overwrite the output file if it already exists
4. **Binary Files**: The program works with any file type - text, images, PDFs, etc.
5. **IV Storage**: The IV is automatically stored in the encrypted file and retrieved during decryption

## Testing and Verification

To verify the encryption/decryption works correctly:

1. Encrypt a file with a password
2. Decrypt it with the same password to a different filename
3. Compare the original and decrypted files - they should be identical

For text files:
```bash
diff message.txt COPY_message.txt
```
(No output means files are identical)

For binary files, you can open both in an image viewer or compare file sizes:
```bash
ls -l smile.png COPY_smile.png
```

## Files Included
- `HW6.java` - Main program source code
- `build.bat` - Windows batch file for compilation
- `run.bat` - Windows batch file for execution
- `README.txt` - This documentation file

## Algorithm Details
- **Cipher**: AES/CBC/PKCS5Padding
- **Key Size**: 256 bits
- **Key Derivation**: PBKDF2WithHmacSHA256
- **Iterations**: 65,536
- **IV Size**: 16 bytes
- **Salt**: "0123456789ABCDEF" (fixed)

## Error Handling
The program handles various error conditions:
- Missing or invalid command-line arguments
- File not found errors
- Invalid passwords (during decryption)
- I/O errors
- Cryptographic errors

## Limitations
- The salt is hard-coded in the program (same for all encryptions)
- The program requires console input for password (not suitable for automation)
- No password strength validation

## Assignment Deliverables Checklist
- [x] Source code (HW6.java)
- [ ] Screenshot: Encrypting message.txt
- [ ] Screenshot: Decrypting to COPY_message.txt
- [ ] Screenshot: Encrypting smile.png
- [ ] Screenshot: Decrypting smile.encrypted
- [ ] Screenshot: Decrypting riddle.encrypted with password IT6780
- [ ] Decrypted riddle.png file

## Troubleshooting

### "No such file or directory"
- Ensure you're in the correct directory where your files are located
- Use `ls` (Linux/Mac) or `dir` (Windows) to verify files exist

### "Wrong password" or decryption fails
- Verify you're using the exact same password used for encryption
- Passwords are case-sensitive

### Compilation errors
- Ensure JDK is properly installed: `java -version`
- Check that all import statements are present

## References
- Java Cryptography Architecture (JCA) Documentation
- AES Standard (FIPS 197)
- PBKDF2 Specification (RFC 2898)
public class Encoding{
    
    public static byte[] hexStringToByteArray(String s) {
    int len = s.length();
    byte[] data = new byte[len / 2];
    for (int i = 0; i < len; i += 2) {
        data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4)
                             + Character.digit(s.charAt(i+1), 16));
    }
    return data;
}

     public static void main(String []args){
        // Finding the character string for hexadecimal encoded string.
        String str = "2f0a";
        System.out.println(hexStringToByteArray(str));
        byte[] bytes = hexStringToByteArray(str);
        String str1 = new String(bytes);
        System.out.println("-------"+str1+"-------");
        System.out.println(str1.split("/").length);
        
        // Finding the Byte array for a string.
        byte[] byteArr = "/".getBytes();
        System.out.println(byteArr);
        String str2 = new String(byteArr);
        System.out.println("-------"+str2+"-------");
        System.out.println(str2.split("/").length);
        
        /* Output - 
        [B@6d06d69c
        -------/
        -------
        2
        [B@7852e922
        -------/-------
        0
        End of output */
     }
}

import java.io.*;
import java.util.Base64;

class AccessTokenUser implements Serializable {
    private final String username;
    private final String accessToken;

    public AccessTokenUser(String username, String accessToken) {
        this.username = username;
        this.accessToken = accessToken;
    }

    public String getUsername() {
        return username;
    }

    public String getAccessToken() {
        return accessToken;
    }
}

class hello {

    public String serialize(AccessTokenUser user) throws IOException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(baos);
        oos.writeObject(user);
        oos.close();
        return Base64.getEncoder().encodeToString(baos.toByteArray());
    }

    public static AccessTokenUser deserialize(String s) throws IOException, ClassNotFoundException {
        byte[] data = Base64.getDecoder().decode(s);
        ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(data));
        AccessTokenUser user = (AccessTokenUser) ois.readObject();
        ois.close();
        return user;
    }

    public static void main(String args[]) {
        String payload = "rO0ABXNyAC9sYWIuYWN0aW9ucy5jb21tb24uc2VyaWFsaXphYmxlLkFjY2Vzc1Rva2VuVXNlchlR/OUSJ6mBAgACTAALYWNjZXNzVG9rZW50ABJMamF2YS9sYW5nL1N0cmluZztMAAh1c2VybmFtZXEAfgABeHB0ACB4bDJpNzBrM3d3c212YmNlZjE0YWRodWY2bWt2MWx4NXQABndpZW5lcg==";
        // AccessTokenUser obj = new AccessTokenUser("wiener", "x2i70k3wwsmvbcef14adhuf6mkv1lx5t");
        // ByteArrayOutputStream baos = new ByteArrayOutputStream();
        // ObjectOutputStream out = new ObjectOutputStream(baos);
        // out.writeObject(obj);
        // out.close();
        // String serialize = Base64.getEncoder().encodeToString(baos.toByteArray());
        // System.out.println(serialize);
        // System.out.println("hello world");
        try {
            AccessTokenUser user = deserialize(payload);
            System.out.println(user.getUsername());
            System.out.println(user.getAccessToken());
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
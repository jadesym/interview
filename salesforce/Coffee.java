import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;
import java.lang.Math;
import java.util.TreeMap;

class Coffee {
    // List<String> records = new ArrayList<String>();
    public static Map<String,Coordinate> cityToCoordinate =  new HashMap<String, Coordinate>();

    public static class Coordinate {
        private double x;
        private double y;

        public Coordinate(double x, double y) {
            this.x = x;
            this.y = y;
        }

        public double getX() {
            return this.x;
        }

        public double getY() {
            return this.y;
        }


    }

    public double getDistance(double firstX, double firstY, double secondX, double secondY) {
        double deltaX = firstX - secondX;
        double deltaY = firstY - secondY;
        return Math.sqrt(deltaX * deltaX + deltaY * deltaY);
    }

    public void printTopThree(String a, String b, String c, double aVal, double bVal, double cVal) {
        System.out.print(a);
        System.out.print(',');
        System.out.println("%.4f", aVal);
        System.out.print(b);
        System.out.print(',');
        System.out.println("%.4f", bVal);
        System.out.print(c);
        System.out.print(',');
        System.out.println("%.4f", cVal);
    }

    public static void main(String[] args){

        Map<Float, String> sortedCoordinates = new TreeMap<Float,String>();
        String filename = args[2];
        try {
            BufferedReader reader = new BufferedReader(new FileReader(filename));
            String line;
            while ((line = reader.readLine()) != null)
            {
              List<String> locationXY = Arrays.asList(line.split(","));
              double distance = getDistance(locationXY.get(1), locationXY.get(2), Double.parseDouble(args[0]), Double.parseDouble(arg[1]));
              sortedCoordinates.put(distance, locationXY.get(0));
            }
            reader.close();
        } catch (Exception e) {
            System.err.format("Exception occurred trying to read '%s'.", filename);
            e.printStackTrace();
        }
        int count = 0;
        for (Map.Entry<Float, String> entry: sortedCoordinates.entrySet()) {
            if (count >= 3) break;
            System.out.print(entry.getValue());
            System.out.print(",");
            System.out.println(entry.getKey());
        }
    }



}

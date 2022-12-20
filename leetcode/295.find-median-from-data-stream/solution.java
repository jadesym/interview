import java.util.PriorityQueue;
import java.util.Comparator;

class StandardComparator implements Comparator<Integer> {
    @Override
    public int compare(Integer a, Integer b) {
        return a - b;
    }
}

class ReverseComparator implements Comparator<Integer> {
    @Override
    public int compare(Integer a, Integer b) {
        return b - a;
    }
}


class MedianFinder {
    // Should store highest value in head to be left side of median
    private PriorityQueue<Integer> lowerPQ;
    // Should store lowest value in head to be right side of median
    private PriorityQueue<Integer> higherPQ;

    public MedianFinder() {
        this.lowerPQ = new PriorityQueue(11, new ReverseComparator());
        this.higherPQ = new PriorityQueue(11, new StandardComparator());
    }

    public void addNum(int num) {
        int lowerPQSize = this.lowerPQ.size();
        int higherPQSize = this.higherPQ.size();

        if (lowerPQSize == 0 && higherPQSize == 0) {
            this.lowerPQ.offer(num);
        } else if (lowerPQSize < higherPQSize) {
            Integer lowestFromHigher = this.higherPQ.peek();

            // Null case can't happen since 0 !> 0
            if (num <= lowestFromHigher) {
                this.lowerPQ.offer(num);
            } else {
                this.higherPQ.offer(num);
                // Null case can't happen since always >= 1
                Integer lowestInHigherPQ = this.higherPQ.poll();
                this.lowerPQ.offer(lowestInHigherPQ);
            }
        } else if (lowerPQSize > higherPQSize) {
            Integer highestFromLower = this.lowerPQ.peek();

            if (num >= highestFromLower) {
                this.higherPQ.offer(num);
            } else {
                this.lowerPQ.offer(num);
                // Null case can't happen since always >= 1
                Integer  highestInLowerPQ = this.lowerPQ.poll();
                this.higherPQ.offer(highestInLowerPQ);
            }
        } else {
            Integer lowestFromHigher = this.higherPQ.peek();
            Integer highestFromLower = this.lowerPQ.peek();

            if (num <= lowestFromHigher) {
                this.lowerPQ.offer(num);
            } else {
                this.higherPQ.offer(num);
            }
        }

    }
    
    public double findMedian() {
        int lowerPQSize = this.lowerPQ.size();
        int higherPQSize = this.higherPQ.size();

        double median;
        if (lowerPQSize < higherPQSize) {
            median  = this.higherPQ.peek();
        } else if (lowerPQSize > higherPQSize) {
            median = this.lowerPQ.peek();
        } else {
            median = (this.higherPQ.peek() + this.lowerPQ.peek()) / 2.0;
        }
        return median;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
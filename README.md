import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mybatis.spring.boot.test.autoconfigure.MybatisTest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.junit.jupiter.SpringExtension;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

@ExtendWith(SpringExtension.class)
@MybatisTest
public class CustomerMapperTest {

    @Autowired
    private CustomerMapper customerMapper;

    @Test
    public void testGetTopCustomersByPointsRedeemed() {
        // Invoke the Mapper method to get the top 5 customers
        List<Customer> topCustomers = customerMapper.getTopCustomersByPointsRedeemed();

        // Check if the list is null or empty
        if (topCustomers == null || topCustomers.isEmpty()) {
            // If the list is null or empty, assert that the size is 0
            assertEquals(0, topCustomers != null ? topCustomers.size() : 0);
        } else {
            // Assert that the list size is less than or equal to 5
            assertTrue(topCustomers.size() <= 5);

            // Check that the customers are ordered correctly based on points redeemed
            int previousPoints = Integer.MAX_VALUE;
            for (Customer customer : topCustomers) {
                assertTrue(customer.getPointsRedeemed() <= previousPoints);
                previousPoints = customer.getPointsRedeemed();
            }
        }
    }
}

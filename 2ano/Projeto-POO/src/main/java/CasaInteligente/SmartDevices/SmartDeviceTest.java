package CasaInteligente.SmartDevices;


import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * The test class SmartDeviceTest.
 *
 * @author  (your name)
 * @version (a version number or a date)
 */
public class SmartDeviceTest {
    /**
     * Default constructor for test class SmartDeviceTest
     */
    public SmartDeviceTest() {
    }

    /**
     * Sets up the test fixture.
     *
     * Called before every test case method.
     */
    @BeforeEach
    public void setUp()
    {
    }

    /**
     * Tears down the test fixture.
     *
     * Called after every test case method.
     */
    @AfterEach
    public void tearDown()
    {
    }
    /*
    @Test
    public void testContructor() {
        SmartDevice smartDev1 = new SmartDevice();
        assertTrue(smartDev1!=null);
        smartDev1 = new SmartDevice("b1", true);
        assertTrue(smartDev1!=null);
        smartDev1 = new SmartDevice("b1", false);
        assertTrue(smartDev1!=null);
    }
    
    @Test
    public void testGetID() {
        SmartDevice smartDev1 = new SmartDevice();
        assertEquals("", smartDev1.getID());
        smartDev1 = new SmartDevice("b1");
        assertEquals("b1", smartDev1.getID());
    }
    
    @Test
    public void testGetOn() {
        SmartDevice smartDev1 = new SmartDevice();
        assertFalse(smartDev1.getOn());
        smartDev1 = new SmartDevice("b1");
        assertFalse(smartDev1.getOn());
        smartDev1 = new SmartDevice("b1");
        assertTrue(smartDev1.getOn());
    }

    @Test
    public void testSetOn() {
        SmartDevice smartDev1 = new SmartDevice("b1");
        smartDev1.setOn(true);
        assertTrue(smartDev1.getOn());
        smartDev1.setOn(false);
        assertFalse(smartDev1.getOn());
    }

     */
}

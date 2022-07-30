package CasaInteligente;

import static org.junit.jupiter.api.Assertions.*;

import CasaInteligente.SmartDevices.SmartBulb;
import CasaInteligente.SmartDevices.SmartSpeaker;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * The test class CasaInteligenteTest.
 *
 * @author  (your name)
 * @version (a version number or a date)
 */
public class CasaInteligenteTest {
    /**
     * Default constructor for test class CasaInteligenteTest
     */
    public CasaInteligenteTest()
    {
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

    @Test
    public void testConstructor() {
        CasaInteligente casaInte1 = new CasaInteligente();
        assertTrue(casaInte1!=null);
        casaInte1 = new CasaInteligente("Campus de Gualtar", 123456789, "EDP");
        assertTrue(casaInte1!=null);
    }
    
    @Test
    public void testAddFindDevice() {
        CasaInteligente casaInte1 = new CasaInteligente("Gualtar", 123456789,"EDP");
        SmartBulb smartBul1 = new SmartBulb("b1");
        SmartSpeaker smartSpe1 = new SmartSpeaker("s1", "102.4", "RUM", 0);
        assertFalse(casaInte1.existsDevice("b1"));
        assertFalse(casaInte1.existsDevice("s1"));
        casaInte1.addDevice(smartBul1, "sala");
        casaInte1.addDevice(smartSpe1, "cozinha");
        assertTrue(casaInte1.existsDevice(smartSpe1.getID()));
        assertTrue(casaInte1.existsDevice(smartBul1.getID()));
    }

    @Test
    public void testGetDevice() {
        CasaInteligente casaInte1 = new CasaInteligente("Gualtar", 123456789, "EDP");
        SmartBulb smartBul1 = new SmartBulb("b1");
        casaInte1.addDevice(smartBul1, "sala");
        assertTrue(casaInte1.getDevice("b1").equals(smartBul1));
    }

    @Test
    public void testSetOn() {
        CasaInteligente casaInte1 = new CasaInteligente("Gualtar", 123456789, "EDP");
        SmartBulb smartBul1 = new SmartBulb("b1");
        assertFalse(smartBul1.getOn());
        casaInte1.addDevice(smartBul1, "cozinha");
        casaInte1.setOn(smartBul1.getID(), true);
        assertTrue(casaInte1.getDevice(smartBul1.getID()).getOn());
    }

    @Test
    public void testSetAllOn() {
        CasaInteligente casaInte1 = new CasaInteligente("Gualtar", 123456789, "EDP");
        SmartBulb smartBul1 = new SmartBulb("b1");
        SmartSpeaker smartSpe1 = new SmartSpeaker("s1", "80.2","RUM", 0);
        casaInte1.addDevice(smartBul1, "sala");
        casaInte1.addDevice(smartSpe1, "quarto");
        assertFalse(casaInte1.getDevice(smartBul1.getID()).getOn());
        assertFalse(casaInte1.getDevice(smartSpe1.getID()).getOn());
        casaInte1.setAllOn(true);
        assertTrue(casaInte1.getDevice(smartBul1.getID()).getOn());
        assertTrue(casaInte1.getDevice(smartSpe1.getID()).getOn());
        casaInte1.setAllOn(false);
        assertFalse(casaInte1.getDevice(smartBul1.getID()).getOn());
        assertFalse(casaInte1.getDevice(smartSpe1.getID()).getOn());
    }

    @Test
    public void testAddRoom() {
        CasaInteligente casaInte1 = new CasaInteligente("Gualtar", 123456789, "EDP");
        casaInte1.addRoom("sala");
        assertTrue(casaInte1.hasRoom("sala"));
        assertFalse(casaInte1.hasRoom("quarto"));
    }

    @Test
    public void testAddToRoom() {
        CasaInteligente casaInte1 = new CasaInteligente("Gualtar", 123456789, "EDP");
        SmartBulb smartBul1 = new SmartBulb("b1");
        SmartSpeaker smartSpe1 = new SmartSpeaker("s1", "92.9","RUM", 0);
        SmartSpeaker smartSpe2 = new SmartSpeaker("s2", "106.5", "RUM", 0);
        casaInte1.addDevice(smartBul1, "sotão");
        casaInte1.addDevice(smartSpe2, "cozinha");
        casaInte1.addRoom("sala");
        casaInte1.addRoom("quarto");
        casaInte1.addDevice(smartSpe1, "sala");
        casaInte1.addDevice(smartBul1, "sala");
        casaInte1.addDevice(smartSpe2, "quarto");
        System.out.println(casaInte1.toString());
        assertTrue(casaInte1.roomHasDevice("sala", smartBul1.getID()));
        assertTrue(casaInte1.roomHasDevice("sala", smartSpe1.getID()));
        assertFalse(casaInte1.roomHasDevice("sala", smartSpe2.getID()));
        assertTrue(casaInte1.roomHasDevice("quarto", smartSpe2.getID()));
    }

    @Test
    public void testRemoveDevice(){
        CasaInteligente casaInte1 = new CasaInteligente("Gualtar", 123456789, "EDP");
        SmartBulb smartBul1 = new SmartBulb("b1");
        SmartSpeaker smartSpe1 = new SmartSpeaker("s1", "92.9","RUM", 0);
        SmartSpeaker smartSpe2 = new SmartSpeaker("s2", "106.5", "RUM", 0);
        casaInte1.addDevice(smartBul1, "sotão");
        casaInte1.addDevice(smartSpe2, "cozinha");
        casaInte1.addRoom("sala");
        casaInte1.addRoom("quarto");
        casaInte1.addDevice(smartSpe1, "sala");
        casaInte1.addDevice(smartBul1, "sala");
        casaInte1.addDevice(smartSpe2, "quarto");
        casaInte1.removeDevice(smartBul1.getID());
        assertFalse(casaInte1.existsDevice(smartBul1.getID()));
    }

    @Test
    public void testeTurnOnDevicesFromLocation(){
        CasaInteligente casaInte1 = new CasaInteligente("Gualtar", 123456789, "EDP");
        SmartBulb smartBul1 = new SmartBulb("b1");
        SmartSpeaker smartSpe1 = new SmartSpeaker("s1", "92.9","RUM", 0);
        SmartSpeaker smartSpe2 = new SmartSpeaker("s2", "106.5", "RUM", 0);
        casaInte1.addDevice(smartBul1, "sotão");
        casaInte1.addDevice(smartSpe2, "cozinha");
        casaInte1.addRoom("sala");
        casaInte1.addRoom("quarto");
        casaInte1.addDevice(smartSpe1, "sala");
        casaInte1.addDevice(smartBul1, "sala");
        casaInte1.addDevice(smartSpe2, "quarto");
        casaInte1.turnOnDevicesFromLocation("sala");
        assertTrue(smartBul1.getOn());
        assertTrue(smartSpe1.getOn());
        assertFalse(smartSpe2.getOn());
    }
}


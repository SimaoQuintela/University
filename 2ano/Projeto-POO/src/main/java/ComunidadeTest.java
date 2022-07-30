import CasaInteligente.CasaInteligente;
import CasaInteligente.SmartDevices.SmartBulb;
import CasaInteligente.SmartDevices.SmartCamera;
import CasaInteligente.SmartDevices.SmartDevice;
import CasaInteligente.SmartDevices.SmartSpeaker;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ComunidadeTest {

    private Comunidade comunidade;

    @BeforeEach
    void setUp() {
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
        this.comunidade = new Comunidade("Braga");
        this.comunidade.addCasa(casaInte1.getProprietario(), casaInte1);
    }

    @AfterEach
    void tearDown() {
    }

    @Test
    public void testEquals(){
        Comunidade comunidade2 = new Comunidade(this.comunidade);
        assertTrue(comunidade2.equals(this.comunidade));
    }
}
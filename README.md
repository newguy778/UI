import org.junit.jupiter.api.Test;
import org.springframework.http.HttpStatus;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.HttpServerErrorException;

import static org.junit.jupiter.api.Assertions.*;

class ExceptionHandlerTest {

    private final ExceptionHandler exceptionHandler = new ExceptionHandler();

    @Test
    void handleConcurrencyFailureException() {
        // Arrange
        ConcurrencyFailureException exception = new ConcurrencyFailureException();
        
        // Act
        ResponseEntity<String> response = exceptionHandler.handleConnversion(exception);
        
        // Assert
        assertEquals(HttpStatus.BAD_REQUEST, response.getStatusCode());
        assertEquals(exception.getMessage(), response.getBody());
    }

    @Test
    void handleHttpClientErrorException_Unauthorized() {
        // Arrange
        HttpClientErrorException exception = new HttpClientErrorException(HttpStatus.UNAUTHORIZED);
        
        // Act
        ResponseEntity<String> response = exceptionHandler.handleUnauthorized(exception);
        
        // Assert 
        assertEquals(HttpStatus.UNAUTHORIZED, response.getStatusCode());
        assertEquals(exception.getMessage(), response.getBody());
    }

    @Test
    void handleHttpClientErrorException_NotFound() {
        // Arrange
        HttpClientErrorException exception = new HttpClientErrorException(HttpStatus.NOT_FOUND);
        
        // Act
        ResponseEntity<String> response = exceptionHandler.handleNotFound(exception);
        
        // Assert
        assertEquals(HttpStatus.NOT_FOUND, response.getStatusCode()); 
        assertEquals(exception.getMessage(), response.getBody());
    }
}

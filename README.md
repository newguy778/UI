@ExtendWith(MockitoExtension.class)
class TransactionServiceTest {
    
    @Mock
    private TransactionMapper transactionMapper;
    
    @InjectMocks
    private TransactionService transactionService;

    @Test
    void getAllTransactionsByDateRange_ReturnsExpectedResult() {
        // Arrange
        String startDate = "2023-01-01";
        String endDate = "2023-12-31";
        ZonedDateTime expectedUtcEndDate = generateExpectedUtcEndDate(startDate, endDate);
        List<Transaction> expectedTransactions = // define expected transactions
        when(transactionMapper.getAllTransactionsByDateRange(startDate, expectedUtcEndDate.toString()))
            .thenReturn(expectedTransactions);

        // Act
        List<Transaction> actualTransactions = transactionService.getAllTransactionsByDateRange(startDate, endDate);

        // Assert
        assertEquals(expectedTransactions, actualTransactions);
        verify(transactionMapper).getAllTransactionsByDateRange(startDate, expectedUtcEndDate.toString());
    }

    private ZonedDateTime generateExpectedUtcEndDate(String startDate, String endDate) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        LocalDate localEndDate = LocalDate.parse(endDate, formatter);
        ZonedDateTime utcEndDate = localEndDate.atStartOfDay(ZoneId.systemDefault())
                .plusDays(1)
                .withZoneSameInstant(ZoneId.of("UTC"));
        
        if (localEndDate.isBefore(LocalDate.parse(startDate, formatter))) {
            throw new IllegalArgumentException("Start date must not be after the end date.");
        }

        return utcEndDate;
    }
}

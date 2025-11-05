import sqlite3
import functools

#### decorator to log SQL queries

def log_queries(func):
    """
    Decorator that logs SQL queries before execution.
    
    Args:
        func: The function to be decorated
        
    Returns:
        wrapper: The wrapped function with logging capability
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the query from kwargs or args
        # First check if 'query' is in kwargs
        if 'query' in kwargs:
            query = kwargs['query']
        # Otherwise, assume it's the first positional argument
        elif args:
            query = args[0]
        else:
            query = "No query provided"
        
        # Log the SQL query
        print(f"Executing SQL Query: {query}")
        
        # Execute the original function
        result = func(*args, **kwargs)
        
        return result
    
    return wrapper


@log_queries
def fetch_all_users(query):
    """
    Fetch all users from the database.
    
    Args:
        query: SQL query string
        
    Returns:
        List of user records
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


#### fetch users while logging the query
# Example usage (uncomment when you have a database set up):
# users = fetch_all_users(query="SELECT * FROM users")
# print(users)
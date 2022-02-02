package com.example.demo.repositories;

import com.example.demo.models.Brand;
import com.example.demo.models.Product;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.DependsOn;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import javax.annotation.PostConstruct;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@DependsOn({"brandRepository"})
@Service
public class ProductRepository {
    @Autowired
    BrandRepository brandRepository;

//    Brand apple = brandRepository.getBrand(1);
//    Brand huawei = brandRepository.getBrand(2);
//    Brand dell = brandRepository.getBrand(3);


    List<Product> PRODUCTS = new ArrayList<>(
            Arrays.asList(
                    new Product(1, "Macbook Pro", null, 12, null),
                    new Product(2, "XPS 13", null, 4, null),
                    new Product(3, "Matebook", null, 25, null),
                    new Product(4, "Ipad Pro", null, 3, null),
                    new Product(5, "Apple Pencil", null, 8, null)
            )
    );

    @PostConstruct
    void updateProducts() {
        PRODUCTS.get(4).setParent(PRODUCTS.get(3));

        PRODUCTS.get(0).setBrand(brandRepository.getBrand(1));
        PRODUCTS.get(1).setBrand(brandRepository.getBrand(3));
        PRODUCTS.get(2).setBrand(brandRepository.getBrand(2));
        PRODUCTS.get(3).setBrand(brandRepository.getBrand(1));
        PRODUCTS.get(4).setBrand(brandRepository.getBrand(1));
    }

    public List<Product> getAllProducts() {
        return PRODUCTS;
    }

    public Product getProduct(Integer id) {
        for (Product product: PRODUCTS) {
            if (product.getId() == id) {
                return product;
            }
        }

        throw new ResponseStatusException(HttpStatus.NOT_FOUND);
    }
}
